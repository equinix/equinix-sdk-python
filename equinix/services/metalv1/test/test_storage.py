# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.storage import Storage

class TestStorage(unittest.TestCase):
    """Storage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Storage:
        """Test Storage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Storage`
        """
        model = Storage()
        if include_optional:
            return Storage(
                disks = [
                    equinix.services.metalv1.models.disk.Disk(
                        device = '', 
                        href = '', 
                        partitions = [
                            equinix.services.metalv1.models.partition.Partition(
                                href = '', 
                                label = '', 
                                number = 56, 
                                size = '', )
                            ], 
                        wipe_table = True, )
                    ],
                filesystems = [
                    equinix.services.metalv1.models.filesystem.Filesystem(
                        href = '', 
                        mount = equinix.services.metalv1.models.mount.Mount(
                            device = '', 
                            format = '', 
                            href = '', 
                            options = [
                                ''
                                ], 
                            point = '', ), )
                    ],
                href = '',
                raid = [
                    equinix.services.metalv1.models.raid.Raid(
                        devices = [
                            ''
                            ], 
                        href = '', 
                        level = '', 
                        name = '', )
                    ]
            )
        else:
            return Storage(
        )
        """

    def testStorage(self):
        """Test Storage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
