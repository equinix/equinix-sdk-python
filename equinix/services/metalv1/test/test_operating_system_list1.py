# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.operating_system_list1 import OperatingSystemList1

class TestOperatingSystemList1(unittest.TestCase):
    """OperatingSystemList1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OperatingSystemList1:
        """Test OperatingSystemList1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperatingSystemList1`
        """
        model = OperatingSystemList1()
        if include_optional:
            return OperatingSystemList1(
                href = '',
                operating_systems = [
                    equinix.services.metalv1.models.operating_system.OperatingSystem(
                        build_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        default_operating_system = True, 
                        deprecation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        distro = '', 
                        distro_label = '', 
                        end_of_life_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        end_of_service_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        href = '', 
                        id = '', 
                        licensed = True, 
                        lifecycle_state = '', 
                        name = '', 
                        preinstallable = True, 
                        pricing = equinix.services.metalv1.models.pricing.pricing(), 
                        provisionable_on = [
                            ''
                            ], 
                        release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        release_notes = '', 
                        slug = '', 
                        version = '', )
                    ]
            )
        else:
            return OperatingSystemList1(
        )
        """

    def testOperatingSystemList1(self):
        """Test OperatingSystemList1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()