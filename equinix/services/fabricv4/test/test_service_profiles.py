# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)
"""

import unittest

from equinix.services.fabricv4.models.service_profiles import ServiceProfiles

class TestServiceProfiles(unittest.TestCase):
    """ServiceProfiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceProfiles:
        """Test ServiceProfiles
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceProfiles`
        """
        model = ServiceProfiles()
        if include_optional:
            return ServiceProfiles(
                data = [
                    equinix.services.fabricv4.models.service_profile.ServiceProfile(
                        state = 'ACTIVE', 
                        account = null, 
                        project = equinix.services.fabricv4.models.project.Project(
                            project_id = '44f4c4f8-2f39-494e-838c-d8e640591be5', ), 
                        change_log = null, )
                    ],
                pagination = equinix.services.fabricv4.models.pagination.Pagination(
                    offset = 0, 
                    limit = 0, 
                    total = 0, 
                    next = '', 
                    previous = '', )
            )
        else:
            return ServiceProfiles(
        )
        """

    def testServiceProfiles(self):
        """Test ServiceProfiles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
