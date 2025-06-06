# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.ip_assignment import IPAssignment

class TestIPAssignment(unittest.TestCase):
    """IPAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IPAssignment:
        """Test IPAssignment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IPAssignment`
        """
        model = IPAssignment()
        if include_optional:
            return IPAssignment(
                address = '',
                address_family = 56,
                assigned_to = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                cidr = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                enabled = True,
                gateway = '',
                global_ip = True,
                href = '',
                id = '',
                manageable = True,
                management = True,
                metro = None,
                netmask = '',
                network = '',
                next_hop = '',
                parent_block = equinix.services.metalv1.models.parent_block.ParentBlock(
                    cidr = 56, 
                    href = '', 
                    netmask = '', 
                    network = '', ),
                public = True,
                state = 'pending'
            )
        else:
            return IPAssignment(
                assigned_to = equinix.services.metalv1.models.href.Href(
                    href = '', ),
        )
        """

    def testIPAssignment(self):
        """Test IPAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
