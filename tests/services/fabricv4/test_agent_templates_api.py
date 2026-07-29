from __future__ import annotations

import pytest

from equinix.services import fabricv4
from .helpers.apis import Apis, for_user
from .helpers.users import UserName

USER_NAME = UserName.PANTHERS_FNV


@pytest.mark.integration
class TestAgentTemplatesApi:
    apis: Apis
    template_uuid: str = None

    @classmethod
    def setup_class(cls) -> None:
        cls.apis = for_user(USER_NAME)
        cls.template_uuid = None

    def test_1_get_agent_templates(self) -> None:
        response = self.apis.agent_templates.get_agent_templates_with_http_info()
        assert response.status_code == 200
        assert response.data is not None
        templates = response.data.data
        assert templates, "No agent templates returned"
        type(self).template_uuid = templates[0].uuid
        assert self.template_uuid is not None, "First agent template has no UUID"

    def test_2_get_agent_template_by_uuid(self) -> None:
        assert self.template_uuid is not None, "No template UUID available from test_1"
        response = self.apis.agent_templates.get_agent_template_by_uuid_with_http_info(
            self.template_uuid
        )
        assert response.status_code == 200
        assert response.data is not None
        assert response.data.uuid == self.template_uuid
        assert isinstance(response.data, fabricv4.AgentTemplates)
