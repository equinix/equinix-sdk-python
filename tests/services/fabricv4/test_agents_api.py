from __future__ import annotations

import pytest

from equinix.services import fabricv4
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FCR


@pytest.mark.integration
class TestAgentsApi:
    apis: Apis
    existing_agent_uuid: str = None

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)
        cls.existing_agent_uuid = None

        response = cls.apis.agents.get_agents()
        agents = response.data
        if agents:
            cls.existing_agent_uuid = agents[0].uuid

    def test_1_get_agents(self) -> None:
        response = self.apis.agents.get_agents_with_http_info()
        assert response.status_code == 200
        assert response.data is not None

    def test_2_get_agent_by_uuid(self) -> None:
        if self.existing_agent_uuid is None:
            pytest.skip("No existing agents found")
        response = self.apis.agents.get_agent_by_uuid_with_http_info(
            self.existing_agent_uuid
        )
        assert response.status_code == 200
        assert response.data is not None
        assert response.data.uuid == self.existing_agent_uuid

    def test_3_get_agent_activities(self) -> None:
        if self.existing_agent_uuid is None:
            pytest.skip("No existing agents found")
        response = self.apis.agents.get_agent_activities_with_http_info(
            self.existing_agent_uuid
        )
        assert response.status_code == 200
        assert response.data is not None
