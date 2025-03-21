# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.instances_batch_create_input_batches_inner import InstancesBatchCreateInputBatchesInner

class TestInstancesBatchCreateInputBatchesInner(unittest.TestCase):
    """InstancesBatchCreateInputBatchesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstancesBatchCreateInputBatchesInner:
        """Test InstancesBatchCreateInputBatchesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstancesBatchCreateInputBatchesInner`
        """
        model = InstancesBatchCreateInputBatchesInner()
        if include_optional:
            return InstancesBatchCreateInputBatchesInner(
                hostnames = [
                    ''
                    ],
                quantity = 56,
                href = '',
                metro = 'sv',
                always_pxe = True,
                billing_cycle = 'hourly',
                customdata = { },
                description = '',
                features = [
                    ''
                    ],
                hardware_reservation_id = 'next-available',
                hostname = '',
                ip_addresses = [
                    equinix.services.metalv1.models.ip_address.IPAddress(
                        address_family = 4, 
                        cidr = 28, 
                        href = '', 
                        ip_reservations = [
                            ''
                            ], 
                        public = False, )
                    ],
                ipxe_script_url = '',
                locked = True,
                network_frozen = True,
                no_ssh_keys = True,
                operating_system = '',
                plan = 'c3.large.x86',
                private_ipv4_subnet_size = 56,
                project_ssh_keys = [
                    ''
                    ],
                public_ipv4_subnet_size = 56,
                spot_instance = True,
                spot_price_max = 1.23,
                ssh_keys = [
                    equinix.services.metalv1.models.ssh_key_input.SSHKeyInput(
                        href = '', 
                        key = '', 
                        label = '', 
                        tags = [
                            ''
                            ], )
                    ],
                storage = equinix.services.metalv1.models.storage.Storage(
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
                        ], ),
                tags = [
                    ''
                    ],
                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_ssh_keys = [
                    ''
                    ],
                userdata = '',
                facility = None
            )
        else:
            return InstancesBatchCreateInputBatchesInner(
                metro = 'sv',
                operating_system = '',
                plan = 'c3.large.x86',
                facility = None,
        )
        """

    def testInstancesBatchCreateInputBatchesInner(self):
        """Test InstancesBatchCreateInputBatchesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
