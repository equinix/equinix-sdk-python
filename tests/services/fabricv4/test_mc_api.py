from __future__ import annotations

import time
import pytest

from equinix.services import fabricv4
from .helpers import utils
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_OMC


@pytest.mark.integration
class TestOMC:
    apis: Apis

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)

    def test_create_omc_bulk(self) -> None:
        response = self.apis.omc.create_bulk_optical_connect(
            fabricv4.BulkOpticalConnectRequest(
                data=[
                    fabricv4.OpticalConnectPostRequest(
                        type=fabricv4.OpticalConnectPostRequestType.OC,
                        pathType=fabricv4.OpticalConnectPostRequestPathType.UNPROTECTED,
                        bandwidth=10000,
                        connectionDestinationType=fabricv4.OpticalConnectPostRequestConnectionDestinationType.REMOTE,
                        aSide=fabricv4.OpticalConnectASideRequest(
                            patchPanelId="PP:0000:1257117",
                            connectorType=fabricv4.OpticalConnectPatchPanelFieldsConnectorType.SC,
                        ),
                        zSide=fabricv4.OpticalConnectZSideRequest(
                            location=fabricv4.OpticalConnectLocation(ibxCode="SV2"),
                            loa=fabricv4.OpticalConnectLOA(
                                uuid="f9605007-6029-46f8-9efd-c7e689be6f7c"
                            ),
                        ),
                        account=fabricv4.SimplifiedAccount(
                            accountNumber=112860,
                            accountName="Fastly, Inc",
                        ),
                        redundancy=fabricv4.OpticalConnectRedundancy(
                            priority=fabricv4.OpticalConnectRedundancyPriority.PRIMARY
                        ),
                    ),
                    fabricv4.OpticalConnectPostRequest(
                        type=fabricv4.OpticalConnectPostRequestType.OC,
                        pathType=fabricv4.OpticalConnectPostRequestPathType.UNPROTECTED,
                        bandwidth=10000,
                        connectionDestinationType=fabricv4.OpticalConnectPostRequestConnectionDestinationType.REMOTE,
                        aSide=fabricv4.OpticalConnectASideRequest(
                            patchPanelId="PP:0001:1213749",
                            connectorType=fabricv4.OpticalConnectPatchPanelFieldsConnectorType.SC,
                        ),
                        zSide=fabricv4.OpticalConnectZSideRequest(
                            location=fabricv4.OpticalConnectLocation(ibxCode="SV2"),
                            loa=fabricv4.OpticalConnectLOA(
                                uuid="f9605007-6029-46f8-9efd-c7e689be6f7c"
                            ),
                        ),
                        account=fabricv4.SimplifiedAccount(
                            accountNumber=112860,
                            accountName="Fastly, Inc",
                        ),
                        redundancy=fabricv4.OpticalConnectRedundancy(
                            priority=fabricv4.OpticalConnectRedundancyPriority.SECONDARY
                        ),
                    ),
                ]
            )
        )
        assert response.data[0].uuid is not None

    def test_create_omc(self) -> None:
        response = self.apis.omc.create_optical_connect(
            fabricv4.OpticalConnectPostRequest(
                type=fabricv4.OpticalConnectPostRequestType.OC,
                pathType=fabricv4.OpticalConnectPostRequestPathType.UNPROTECTED,
                bandwidth=10000,
                connectionDestinationType=fabricv4.OpticalConnectPostRequestConnectionDestinationType.REMOTE,
                aSide=fabricv4.OpticalConnectASideRequest(
                    patchPanelId="PP:0000:1257117",
                    connectorType=fabricv4.OpticalConnectPatchPanelFieldsConnectorType.SC,
                ),
                zSide=fabricv4.OpticalConnectZSideRequest(
                    location=fabricv4.OpticalConnectLocation(ibxCode="SV2"),
                    loa=fabricv4.OpticalConnectLOA(
                        uuid="f9605007-6029-46f8-9efd-c7e689be6f7c"
                    ),
                ),
                account=fabricv4.SimplifiedAccount(
                    accountNumber=112860,
                    accountName="Fastly, Inc",
                ),
            ),
        )
        assert response.uuid is not None

    def test_get_omc(self) -> None:
        response = self.apis.omc.get_optical_connect_by_uuid(
            optical_connect_id="cd1eee2a-ec46-47f4-a313-d18e6d21fa88"
        )
        assert response.uuid == "cd1eee2a-ec46-47f4-a313-d18e6d21fa88"

    def test_search_omc(self) -> None:
        response = self.apis.omc.search_optical_connect(
            fabricv4.OpticalConnectSearchRequest(
                filter=fabricv4.OpticalConnectFilters(
                    var_and=[
                        fabricv4.OpticalConnectFilter(
                            fabricv4.OpticalConnectSimpleExpression(
                                property="/uuid",
                                operator="=",
                                values=["cd1eee2a-ec46-47f4-a313-d18e6d21fa88"],
                            )
                        )
                    ],
                ),
                pagination=fabricv4.PaginationRequest(offset=0, limit=100),
            )
        )

        services = response.data
        assert services, "Search returned no OMC"

        assert len(services) == 1, "More than 1 OMC returned"
        assert (
            services[0].uuid == "cd1eee2a-ec46-47f4-a313-d18e6d21fa88"
        ), "Wrong OMC returned"
