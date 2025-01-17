# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.disk import Disk

class TestDisk(unittest.TestCase):
    """Disk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Disk:
        """Test Disk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Disk`
        """
        model = Disk()
        if include_optional:
            return Disk(
                device = '',
                href = '',
                partitions = [
                    equinix.services.metalv1.models.partition.Partition(
                        href = '', 
                        label = '', 
                        number = 56, 
                        size = '', )
                    ],
                wipe_table = True
            )
        else:
            return Disk(
        )
        """

    def testDisk(self):
        """Test Disk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
