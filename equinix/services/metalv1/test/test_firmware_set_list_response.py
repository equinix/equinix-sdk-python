# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.firmware_set_list_response import FirmwareSetListResponse

class TestFirmwareSetListResponse(unittest.TestCase):
    """FirmwareSetListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirmwareSetListResponse:
        """Test FirmwareSetListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirmwareSetListResponse`
        """
        model = FirmwareSetListResponse()
        if include_optional:
            return FirmwareSetListResponse(
                href = '',
                page = 56,
                page_count = 56,
                page_size = 56,
                records = [
                    equinix.services.metalv1.models.firmware_set.FirmwareSet(
                        attributes = [
                            equinix.services.metalv1.models.attribute.Attribute(
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                data = equinix.services.metalv1.models.attribute_data.AttributeData(
                                    href = '', 
                                    latest = True, 
                                    model = '', 
                                    plan = '', 
                                    vendor = '', ), 
                                href = '', 
                                namespace = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        component_firmware = [
                            equinix.services.metalv1.models.component.Component(
                                checksum = '', 
                                component = 'bmc', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                filename = '', 
                                href = '', 
                                model = [
                                    'romed8hm3'
                                    ], 
                                repository_url = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                upstream_url = '', 
                                uuid = '0516463a-47ee-4809-9a66-ece8c740eed9', 
                                vendor = 'equinix', 
                                version = '1.5.0', )
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        name = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        uuid = '0516463a-47ee-4809-9a66-ece8c740eed9', )
                    ],
                total_pages = 56,
                total_record_count = 56
            )
        else:
            return FirmwareSetListResponse(
        )
        """

    def testFirmwareSetListResponse(self):
        """Test FirmwareSetListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
