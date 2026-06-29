from __future__ import annotations

import time

import pytest

from equinix.services import fabricv4
from equinix.services.fabricv4.exceptions import ApiException
from .helpers import utils
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FNV
IA_METRO = "SV"
DELETE_RETRY_INTERVAL_S = 10
DELETE_MAX_ATTEMPTS = 6
STATE_RETRY_INTERVAL_S = 5
STATE_MAX_ATTEMPTS = 5
CONNECTION_RETRY_INTERVAL_S = 20
CONNECTION_MAX_ATTEMPTS = 15
CONNECTION_CREATE_MAX_ATTEMPTS = 5
DUPLICATE_VLAN_ERROR_CODE = "EQ-3142570"
CONNECTION_ALREADY_DELETED_ERROR_CODE = "EQ-3142509"
INITIAL_BANDWIDTH = 50
BANDWIDTH_CANDIDATES = (100, 200, 500, 1000)


def _value(enum_or_str):
    return getattr(enum_or_str, "value", enum_or_str)


@pytest.mark.integration
class TestInternetAccessApi:
    apis: Apis
    test_data = None
    created_service_uuid = None
    created_ip_block_uuid = None
    created_connection_uuids: list = []

    @classmethod
    def setup_class(cls) -> None:
        cls.test_data = utils.get_user_data(USER_NAME)
        cls.apis = for_user(USER_NAME)
        cls.created_service_uuid = None
        cls.created_ip_block_uuid = None
        cls.created_connection_uuids = []

    @classmethod
    def teardown_class(cls) -> None:
        service_deleted = cls._wait_for_service_deleted()
        cls._delete_created_connections()
        cls._delete_created_ip_block()
        assert service_deleted, (
            f"Internet Access Service {cls.created_service_uuid} was not deleted"
        )

    def test_1_create_eia_service(self) -> None:
        service = self._create_internet_access_service()
        type(self).created_service_uuid = service.uuid
        assert self.created_service_uuid is not None, (
            "Created Internet Access Service has no UUID"
        )

    def test_2_get_eia_service(self) -> None:
        assert self.created_service_uuid is not None, "No Internet Access Service was created"
        response = self.apis.internet_access_services.get_eia_service_with_http_info(
            self.created_service_uuid
        )
        assert response.status_code == 200
        assert response.data.uuid == self.created_service_uuid

    def test_3_search_eia_services(self) -> None:
        assert self.created_service_uuid is not None, "No Internet Access Service was created"
        response = self._search_services()
        services = response.data
        assert response.status_code == 200
        assert services.data, "Search returned no services"
        assert all(
            s.state == fabricv4.InternetAccessServiceState.PROVISIONED for s in services.data
        ), "Search returned services that are not PROVISIONED"
        found = any(s.uuid == self.created_service_uuid for s in services.data)
        assert found, (
            f"Created Internet Access Service {self.created_service_uuid} "
            f"not found in search results"
        )

    def test_4_patch_eia_service(self) -> None:
        assert self.created_service_uuid is not None, "No Internet Access Service was created"

        for bandwidth in BANDWIDTH_CANDIDATES:
            operation = fabricv4.InternetAccessPatchOperationUpdate(
                op=fabricv4.InternetAccessPatchOperationUpdateAllowedOp.REPLACE,
                path="/bandwidth",
                value=bandwidth,
            )
            try:
                response = self.apis.internet_access_services.patch_eia_service_with_http_info(
                    self.created_service_uuid, [operation]
                )
                assert response.status_code == 202
                return
            except ApiException as e:
                body = str(e.body)
                if "EQ-7100076" in body:
                    continue
                if "EQ-7100077" in body:
                    time.sleep(STATE_RETRY_INTERVAL_S)
                    continue
                raise
        pytest.fail(
            f"Could not patch bandwidth to a new value for service {self.created_service_uuid}"
        )

    def test_5_delete_eia_service(self) -> None:
        assert self.created_service_uuid is not None, "No Internet Access Service was created"
        assert self._wait_for_service_is_in_state(
            self.created_service_uuid, fabricv4.InternetAccessServiceState.PROVISIONED
        ), "Internet Access Service was not PROVISIONED before delete"
        assert self._delete_eia_service(self.created_service_uuid), (
            "Internet Access Service was not deleted in time"
        )

    @classmethod
    def _wait_for_service_deleted(cls) -> bool:
        if cls.created_service_uuid is None:
            return True
        for attempt in range(1, DELETE_MAX_ATTEMPTS + 1):
            try:
                state = cls.apis.internet_access_services.get_eia_service(
                    cls.created_service_uuid
                ).state
                if state == fabricv4.InternetAccessServiceState.DEPROVISIONED:
                    return True
            except ApiException as e:
                if e.status == 404:
                    return True
                print(f"Service delete check attempt {attempt} "
                      f"for {cls.created_service_uuid}: {e}")
            time.sleep(DELETE_RETRY_INTERVAL_S)
        print(f"Internet Access Service {cls.created_service_uuid} "
              f"was not deprovisioned within the timeout")
        return False

    @classmethod
    def _delete_created_ip_block(cls) -> None:
        if cls.created_ip_block_uuid is None:
            return
        for attempt in range(1, DELETE_MAX_ATTEMPTS + 1):
            try:
                response = cls.apis.ip_blocks.delete_ip_block_by_id_with_http_info(
                    cls.created_ip_block_uuid
                )
                if response.status_code // 100 == 2:
                    return
            except ApiException as e:
                print(f"Ip block delete attempt {attempt} "
                      f"for {cls.created_ip_block_uuid} not ready: {e}")
            time.sleep(DELETE_RETRY_INTERVAL_S)
        print(f"Ip block {cls.created_ip_block_uuid} could not be deleted within the timeout")

    @classmethod
    def _delete_created_connections(cls) -> None:
        for connection_uuid in list(cls.created_connection_uuids):
            deleted = False
            for attempt in range(1, DELETE_MAX_ATTEMPTS + 1):
                try:
                    response = cls.apis.connections.delete_connection_by_uuid_with_http_info(
                        connection_uuid
                    )
                    if response.status_code // 100 == 2:
                        deleted = True
                        break
                except ApiException as e:
                    if e.status == 404 or CONNECTION_ALREADY_DELETED_ERROR_CODE in str(e.body):
                        deleted = True
                        break
                    print(f"Connection delete attempt {attempt} "
                          f"for {connection_uuid} not ready: {e}")
                time.sleep(DELETE_RETRY_INTERVAL_S)
            if not deleted:
                print(f"Connection {connection_uuid} could not be deleted within the timeout")

    def _search_services(self):
        request_body = fabricv4.InternetAccessSearchRequest(
            filter=fabricv4.SearchExpression(
                var_and=[
                    fabricv4.SearchExpression(
                        var_property="/project/projectId",
                        operator="=",
                        values=[self.test_data.project_id],
                    ),
                    fabricv4.SearchExpression(
                        var_property="/state",
                        operator="=",
                        values=[
                            _value(fabricv4.InternetAccessServiceState.PROVISIONED)
                        ],
                    ),
                ]
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        return self.apis.internet_access_services.search_eia_services_with_http_info(request_body)

    @classmethod
    def _wait_for_service_is_in_state(cls, uuid, expected_state) -> bool:
        current_state = None
        for _ in range(STATE_MAX_ATTEMPTS):
            try:
                service = cls.apis.internet_access_services.get_eia_service(uuid)
                current_state = service.state
            except ApiException as e:
                print(f"Service state check for {uuid} not ready: {e}")
                time.sleep(STATE_RETRY_INTERVAL_S)
                continue
            if current_state == expected_state:
                return True
            time.sleep(STATE_RETRY_INTERVAL_S)
        print(f"Internet Access Service {uuid} did not reach {expected_state} state "
              f"(current: {current_state})")
        return False

    def _create_ia_connection(self) -> str:
        port = self._select_dot1q_port()

        connection = None
        for _ in range(CONNECTION_CREATE_MAX_ATTEMPTS):
            connection_post_request = fabricv4.ConnectionPostRequest(
                name=f"panthers-eia-con-{utils.get_random_vlan_number()}",
                type=fabricv4.ConnectionType.IA_VC,
                bandwidth=INITIAL_BANDWIDTH,
                project=fabricv4.Project(project_id=self.test_data.project_id),
                notifications=[
                    fabricv4.SimplifiedNotification(
                        type="ALL", emails=["panthers_auto@equinix.com"]
                    )
                ],
                a_side=fabricv4.ConnectionSide(
                    access_point=fabricv4.AccessPoint(
                        type=fabricv4.AccessPointType.COLO,
                        port=fabricv4.SimplifiedPort(uuid=port.uuid),
                        link_protocol=fabricv4.SimplifiedLinkProtocol(
                            type=fabricv4.LinkProtocolType.DOT1Q,
                            vlan_tag=utils.get_random_vlan_number(),
                        ),
                    )
                ),
                z_side=fabricv4.ConnectionSide(
                    access_point=fabricv4.AccessPoint(
                        type=fabricv4.AccessPointType.SP,
                        profile=fabricv4.SimplifiedServiceProfile(
                            type=fabricv4.ServiceProfileTypeEnum.IA_PROFILE,
                            uuid=self.test_data.ia_profile_uuid,
                        ),
                        location=fabricv4.SimplifiedLocation(metro_code=IA_METRO),
                    )
                ),
            )
            try:
                response = self.apis.connections.create_connection_with_http_info(
                    connection_post_request, dry_run=False
                )
            except ApiException as e:
                # Duplicate VLAN on the port — pick a new VLAN and retry.
                if e.status == 400 and DUPLICATE_VLAN_ERROR_CODE in str(e.body):
                    print(f"Connection create hit duplicate VLAN, retrying: {e.body}")
                    continue
                raise
            if response.status_code == 201:
                connection = response.data
                break

        assert connection is not None, (
            "Could not create IA connection (VLAN conflicts or non-201 response)"
        )
        type(self).created_connection_uuids.append(connection.uuid)
        assert self._wait_for_connection_is_in_state(
            connection.uuid, fabricv4.EquinixStatus.PROVISIONED
        ), f"Connection {connection.uuid} did not reach PROVISIONED state"
        return connection.uuid

    def _wait_for_connection_is_in_state(self, connection_uuid, *connection_state) -> bool:
        result = False
        current_state = None
        for _ in range(CONNECTION_MAX_ATTEMPTS):
            try:
                connection = self.apis.connections.get_connection_by_uuid(connection_uuid)
                current_state = connection.operation.equinix_status
            except ApiException as e:
                print(f"Connection state check for {connection_uuid} not ready: {e}")
                time.sleep(CONNECTION_RETRY_INTERVAL_S)
                continue
            if current_state in connection_state:
                result = True
                break
            time.sleep(CONNECTION_RETRY_INTERVAL_S)
        if not result:
            print(f"Connection has not reached the expected state: "
                  f"{_value(connection_state[0])} current state: {_value(current_state)}")
        return result

    def _select_dot1q_port(self):
        ports = [
            p for p in self._get_ports().data
            if p.location is not None and p.location.metro_code == IA_METRO
            and p.encapsulation is not None and _value(p.encapsulation.type) == "DOT1Q"
        ]
        assert ports, f"No DOT1Q port available in metro {IA_METRO}"
        return ports[0]

    def _get_ports(self):
        port_search_request = fabricv4.PortV4SearchRequest(
            filter=fabricv4.PortExpression(
                var_or=[
                    fabricv4.PortExpression(
                        var_and=[
                            fabricv4.PortExpression(
                                operator="=",
                                var_property=fabricv4.PortSearchFieldName.SLASH_STATE,
                                values=["ACTIVE"],
                            ),
                            fabricv4.PortExpression(
                                operator="=",
                                var_property=(
                                    fabricv4.PortSearchFieldName.SLASH_PROJECT_SLASH_PROJECT_ID
                                ),
                                values=[self.test_data.project_id],
                            ),
                            fabricv4.PortExpression(
                                operator="=",
                                var_property=(
                                    fabricv4.PortSearchFieldName.SLASH_LOCATION_SLASH_METRO_CODE
                                ),
                                values=[IA_METRO],
                            ),
                        ]
                    )
                ]
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
            sort=[
                fabricv4.PortSortCriteria(
                    var_property=fabricv4.PortSortBy.SLASH_DEVICE_SLASH_NAME,
                    direction=fabricv4.PortSortDirection.DESC,
                )
            ],
        )
        return self.apis.ports.search_ports(port_search_request)

    def _create_customer_ipv4_block(self):
        prefix = f"67.223.{1 + (utils.get_random_vlan_number() % 254)}.0/24"
        request_body = fabricv4.SubmitIpBlockRequestBody(
            type=fabricv4.TypeOfIpBlockProduct.IPV4_IP_BLOCK,
            prefix=prefix,
            project=fabricv4.IpBlockProjectRequest(project_id=self.test_data.project_id),
        )
        response = self.apis.ip_blocks.submit_ip_block_with_http_info(request_body)
        assert response.status_code == 202
        ip_block = response.data
        type(self).created_ip_block_uuid = ip_block.uuid
        return ip_block

    @staticmethod
    def _equinix_peer_ip_for(ip_block) -> str:
        octets = ip_block.prefix.split("/")[0].split(".")
        return f"{octets[0]}.{octets[1]}.{octets[2]}.5"

    @classmethod
    def _delete_eia_service(cls, uuid) -> bool:
        for attempt in range(1, DELETE_MAX_ATTEMPTS + 1):
            try:
                state = cls.apis.internet_access_services.get_eia_service(uuid).state
                if state in (
                        fabricv4.InternetAccessServiceState.DEPROVISIONED,
                        fabricv4.InternetAccessServiceState.DEPROVISIONING,
                ):
                    return True
                response = (
                    cls.apis.internet_access_services.delete_eia_service_with_http_info(uuid)
                )
                if response.status_code // 100 == 2:
                    return True
            except ApiException as e:
                print(f"Delete attempt {attempt} for {uuid} not ready: {e}")
            time.sleep(DELETE_RETRY_INTERVAL_S)
        print(f"Internet Access Service {uuid} could not be deleted within the timeout")
        return False

    def _create_internet_access_service(self):
        connection_uuid = self._create_ia_connection()
        ip_block = self._create_customer_ipv4_block()
        equinix_peer_ip = self._equinix_peer_ip_for(ip_block)

        routing_protocol = fabricv4.InternetAccessRoutingProtocolDirectRequest(
            type=fabricv4.InternetAccessRoutingProtocolType.DIRECT,
            connections=[
                fabricv4.InternetAccessConnectionDirectRequest(
                    uuid=connection_uuid,
                    peering_ipv4=fabricv4.InternetAccessPeeringIpv4Request(
                        equinix_peer_ip=equinix_peer_ip
                    ),
                )
            ],
            customer_routes=[
                fabricv4.InternetAccessCustomerRouteRequest(
                    ip_block=fabricv4.InternetAccessIpBlockRequest(uuid=ip_block.uuid)
                )
            ],
        )

        request_body = fabricv4.InternetAccessPostRequest(
            type=fabricv4.InternetAccessServiceType.SINGLE_IA,
            name=f"panthers_eia_{utils.get_random_vlan_number()}",
            bandwidth=INITIAL_BANDWIDTH,
            routing_protocol=routing_protocol,
            billing=fabricv4.InternetAccessPostRequestBilling(
                type=fabricv4.InternetAccessBillingType.FIXED
            ),
            project=fabricv4.Project(project_id=self.test_data.project_id),
            account=fabricv4.InternetAccessAccount(
                account_number=self.test_data.account_number_eia
            ),
        )

        response = self.apis.internet_access_services.create_eia_service_with_http_info(
            request_body
        )
        service = response.data
        assert response.status_code == 201

        type(self).created_service_uuid = service.uuid

        assert self._wait_for_service_is_in_state(
            service.uuid, fabricv4.InternetAccessServiceState.PROVISIONED
        ), "Internet Access Service did not reach PROVISIONED state"
        return service
