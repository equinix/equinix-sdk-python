from __future__ import annotations

import time
import pytest

from equinix.services import fabricv4
from .helpers import utils
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FCR

@pytest.mark.integration
class TestCrossConnect:
    apis: Apis

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)

    def test_get_cross_connect(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8"
        )
        assert response.uuid == "47a8bc62-501c-4e07-a852-536ef472a6a8"

    def test_search_cross_connect(self) -> None:
        request_body = fabricv4.CrossConnectSearchRequest(
            filter=fabricv4.CrossConnectSearchFilters(
                    var_and=[fabricv4.CrossConnectFilter(fabricv4.CrossConnectSearchSimpleExpressions(
                    property=fabricv4.CrossConnectFieldName.SLASH_TYPE,
                    operator=fabricv4.LoaSimpleExpressionOperator.EQUAL,
                    values=["XC"],
                ))],
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        response = self.apis.cross_connect.search_cross_connects(request_body)

        services = response.data
        assert services, "Search returned no services"

        assert len(services) > 0

    def test_get_cross_connect_schedules(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_schedules_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8"
        )
        assert response.data[0].uuid == "847fdc96-4c4f-4015-b90f-a8f126d3ecd2"

    def test_get_cross_connect_services(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_services_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8"
        )
        assert response.data == []

    def test_get_cross_connect_attachments(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_attachments_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8"
        )
        assert response.data == []

    def test_get_cross_connect_notes(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_notes_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8"
        )
        assert response.data[0].uuid == "a74388c5-a1f7-42c0-961a-09eb037ff447"

    def test_search_cross_connect_actions(self) -> None:
        request_body = fabricv4.CrossConnectActionSearchRequest(
            filter=fabricv4.CrossConnectActionSearchFilters(
                    var_and=[fabricv4.CrossConnectActionFilter(fabricv4.CrossConnectActionSearchSimpleExpressions(
                    property=fabricv4.CrossConnectActionFieldName.SLASH_TYPE,
                    operator=fabricv4.LoaActionSearchSimpleExpressionsOperator.EQUAL,
                    values=["XC_INFORMATION_UPDATE"],
                ))],
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        response = self.apis.cross_connect.search_cross_connect_action("47a8bc62-501c-4e07-a852-536ef472a6a8", request_body)

        services = response.data
        assert services, "Search returned no actions"

        assert services[0].uuid == "90a89c56-44ce-4f66-902c-0f96813095f3", "Wrong action returned"

    def test_get_cross_connect_action(self) -> None:
        response = self.apis.cross_connect.get_cross_connect_action_by_uuid(
            "47a8bc62-501c-4e07-a852-536ef472a6a8",
            "90a89c56-44ce-4f66-902c-0f96813095f3",
        )

        assert response.uuid == "90a89c56-44ce-4f66-902c-0f96813095f3"

    def test_search_cross_connect_schedules(self) -> None:
        request_body = fabricv4.CrossConnectScheduleSearchRequest(
            filter=fabricv4.CrossConnectScheduleSearchFilters(
                    var_and=[
                        fabricv4.CrossConnectScheduleSearchSimpleExpressions(
                            property=fabricv4.CrossConnectScheduleFieldName.SLASH_TYPE,
                            operator=fabricv4.CrossConnectScheduleSearchSimpleExpressionsOperator.EQUAL,
                            values=["XC_INSTALL_SCHEDULE"],
                        ),
                        fabricv4.CrossConnectScheduleSearchSimpleExpressions(
                            property=fabricv4.CrossConnectScheduleFieldName.SLASH_A_SIDE_SLASH_LOCATION_SLASH_IBX_CODE,
                            operator=fabricv4.CrossConnectScheduleSearchSimpleExpressionsOperator.EQUAL,
                            values=["SV1"],
                        ),
                        fabricv4.CrossConnectScheduleSearchSimpleExpressions(
                            property=fabricv4.CrossConnectScheduleFieldName.SLASH_Z_SIDE_SLASH_LOCATION_SLASH_IBX_CODE,
                            operator=fabricv4.CrossConnectScheduleSearchSimpleExpressionsOperator.EQUAL,
                            values=["SV1"],
                        ),
                        ],
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        response = self.apis.cross_connect.search_cross_connect_schedules(request_body)

        assert response.pagination.total > 0
