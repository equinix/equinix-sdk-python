# coding: utf-8

"""
    Equinix Fabric API v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.fabricv4.models.precision_time_package_response import PrecisionTimePackageResponse

class TestPrecisionTimePackageResponse(unittest.TestCase):
    """PrecisionTimePackageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrecisionTimePackageResponse:
        """Test PrecisionTimePackageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrecisionTimePackageResponse`
        """
        model = PrecisionTimePackageResponse()
        if include_optional:
            return PrecisionTimePackageResponse(
                href = '',
                type = 'TIME_SERVICE_PACKAGE',
                code = 'NTP_STANDARD',
                bandwidth = 10,
                clients_per_second_max = 100,
                redundancy_supported = False,
                multi_subnet_supported = True,
                accuracy_sla_unit = 'microseconds',
                accuracy_sla = 50,
                accuracy_sla_min = 1,
                accuracy_sla_max = 10,
                changelog = equinix.services.fabricv4.models.changelog.Changelog(
                    created_by = 'johnsmith', 
                    created_by_full_name = 'John Smith', 
                    created_by_email = 'john.smith@example.com', 
                    created_date_time = '2020-11-06T07:00Z', 
                    updated_by = 'johnsmith', 
                    updated_by_full_name = 'John Smith', 
                    updated_by_email = 'john.smith@example.com', 
                    updated_date_time = '2020-11-06T07:00Z', 
                    deleted_by = 'johnsmith', 
                    deleted_by_full_name = 'John Smith', 
                    deleted_by_email = 'john.smith@example.com', 
                    deleted_date_time = '2020-11-06T07:00Z', )
            )
        else:
            return PrecisionTimePackageResponse(
                type = 'TIME_SERVICE_PACKAGE',
                code = 'NTP_STANDARD',
                bandwidth = 10,
        )
        """

    def testPrecisionTimePackageResponse(self):
        """Test PrecisionTimePackageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
