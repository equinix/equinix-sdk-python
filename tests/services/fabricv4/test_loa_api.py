from __future__ import annotations

import pytest

from equinix.services import fabricv4
from .helpers import utils
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FCR

@pytest.mark.integration
class TestLoa:
    apis: Apis

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)

    def test_create_loa(self) -> None:
        request_body = fabricv4.CreateLoa(
                fabricv4.RequestLoa(
            type=fabricv4.LoaType.CAGE_LOA,
            name=f"AccRes_{utils.get_random_vlan_number()}",
            description="LOA created by tests",
            authorizedProductType=fabricv4.LoaProductType.XC,
            location=fabricv4.LoaLocation(ibxCode="SV1"),
            )
        )

        response = self.apis.loa.create_loa(request_body)
        assert response.uuid is not None

    def test_get_loa(self) -> None:
        response = self.apis.loa.get_loa_by_uuid(
            "c30a9284-b685-403e-bc0b-77e3d6070408"
        )
        assert response.uuid == "c30a9284-b685-403e-bc0b-77e3d6070408"

    def test_search_loa(self) -> None:
        request_body = fabricv4.LoaSearchRequest(
            filter=fabricv4.LoaSearchFilters(
                var_and=[
                        fabricv4.LoaFilter(
                        fabricv4.LoaSimpleExpression(
                        property=fabricv4.LoaFieldName.SLASH_UUID,
                        operator=fabricv4.LoaSimpleExpressionOperator.EQUAL,
                        values=["c30a9284-b685-403e-bc0b-77e3d6070408"],
                        ),
                    ),
                ]
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        response = self.apis.loa.search_loa(request_body)


        services = response.data
        assert services, "Search returned no services"

        assert len(services) == 1, "More than 1 LOA returned"
        assert services[0].uuid == "c30a9284-b685-403e-bc0b-77e3d6070408", "Wrong LOA record returned"

    def test_update_loa(self) -> None:
        new_name ="AccDep_{utils.get_random_vlan_number()}"

        response = self.apis.loa.update_loa_by_uuid("c30a9284-b685-403e-bc0b-77e3d6070408", [fabricv4.LoaReplaceOperation.model_construct(
                op=fabricv4.LoaOpEnum.REPLACE,
                path="/name",
                value=new_name,
            )])

        assert response.name == new_name

    def test_create_loa_note(self) -> None:
        response = self.apis.loa.create_loa_note_by_loa_id("c30a9284-b685-403e-bc0b-77e3d6070408", fabricv4.CreateLoaNote(comments="note created by tests"))

        assert response.comments == "note created by tests"

    def test_get_loa_notes(self) -> None:
        response = self.apis.loa.get_loa_notes_by_uuid("c30a9284-b685-403e-bc0b-77e3d6070408")

        assert "a2ed6261-1c14-4896-b77b-f3f10fc99243" in map(lambda d: d.uuid, response.data or []), "created note not found"

    def test_create_loa_action(self) -> None:
        response = self.apis.loa.perform_loa_action("c30a9284-b685-403e-bc0b-77e3d6070408", fabricv4.LoaActionRequest(type=fabricv4.LoaActionType.LOA_COPY_LINK))

        assert response.type == fabricv4.LoaActionType.LOA_COPY_LINK

    def test_search_loa_action(self) -> None:
        response = self.apis.loa.search_loa_action("c30a9284-b685-403e-bc0b-77e3d6070408", fabricv4.LoaActionSearchRequest(
                filter=fabricv4.LoaActionSearchFilters(
                     var_and=[
                             fabricv4.LoaActionFilter(
                             fabricv4.LoaActionSearchSimpleExpressions(
                             property=fabricv4.LoaActionFieldName.SLASH_UUID,
                             operator=fabricv4.LoaActionSearchSimpleExpressionsOperator.EQUAL,
                             values=["13a7b3b2-c48e-4053-ab8d-0cfe19b90585"],
                             ),
                         ),
                     ]
                 )
            ))

        assert len(response.data) == 1, "More than 1 LOA returned"
        assert response.data[0].uuid == "13a7b3b2-c48e-4053-ab8d-0cfe19b90585", "expected LOA action not found"

    def test_get_loa_action(self) -> None:
        response = self.apis.loa.get_loa_actions_by_uuid("c30a9284-b685-403e-bc0b-77e3d6070408",  "13a7b3b2-c48e-4053-ab8d-0cfe19b90585")

        assert response.uuid == "13a7b3b2-c48e-4053-ab8d-0cfe19b90585", "expected LOA action not found"

    def test_get_loa_consumer(self) -> None:
        response = self.apis.loa.get_loa_consumers_by_loa_id("c30a9284-b685-403e-bc0b-77e3d6070408")

        assert response.data == []
