# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.ssh_key_list import SSHKeyList

class TestSSHKeyList(unittest.TestCase):
    """SSHKeyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SSHKeyList:
        """Test SSHKeyList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SSHKeyList`
        """
        model = SSHKeyList()
        if include_optional:
            return SSHKeyList(
                href = '',
                ssh_keys = [
                    equinix.services.metalv1.models.ssh_key.SSHKey(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        entity = equinix.services.metalv1.models.href.Href(
                            href = '', ), 
                        fingerprint = '', 
                        href = '', 
                        id = '', 
                        key = '', 
                        label = '', 
                        tags = [
                            ''
                            ], 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return SSHKeyList(
        )
        """

    def testSSHKeyList(self):
        """Test SSHKeyList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
