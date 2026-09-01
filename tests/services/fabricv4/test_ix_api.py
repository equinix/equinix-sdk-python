from __future__ import annotations

import time
import pytest

from equinix.services import fabricv4
from .helpers import utils
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FCR

@pytest.mark.integration
class TestIX:
    apis: Apis

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)

    def test_1_get_ix(self) -> None:
        response = self.apis.ix.get_exchange_service_by_id(
            "01a0428c-5b8c-7d62-8b16-20487363af77"
        )
        assert response.uuid == "01a0428c-5b8c-7d62-8b16-20487363af77"

    def test_2_search_ix(self) -> None:
        request_body = fabricv4.ExchangeServiceSearchRequest(
            filter=fabricv4.ExchangeServiceSearchExpression(
                    fabricv4.ExchangeServicePropertyExpression(
                    property=fabricv4.ExchangeServicePropertyExpressionProperty.SLASH_PROJECT_SLASH_PROJECT_ID,
                    operator=fabricv4.ExchangeServicePropertyExpressionOperator.EQUAL,
                    values=["33ec651f-cc99-48e0-94d3-47466899cdc7"],
                ),
            ),
            pagination=fabricv4.PaginationRequest(offset=0, limit=100),
        )
        response = self.apis.ix.search_exchange_service(request_body)

        services = response.data
        assert services, "Search returned no services"

        assert len(services) == 1, "More than 1 service returned"
        assert services[0].uuid == "01a0428c-5b8c-7d62-8b16-20487363af77", "Wrong service returned"
