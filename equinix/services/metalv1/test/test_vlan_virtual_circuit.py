# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vlan_virtual_circuit import VlanVirtualCircuit

class TestVlanVirtualCircuit(unittest.TestCase):
    """VlanVirtualCircuit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VlanVirtualCircuit:
        """Test VlanVirtualCircuit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VlanVirtualCircuit`
        """
        model = VlanVirtualCircuit()
        if include_optional:
            return VlanVirtualCircuit(
                bill = True,
                bill_type = 'metal_billed',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                href = '',
                id = '',
                name = '',
                nni_vlan = 56,
                port = equinix.services.metalv1.models.interconnection_port.InterconnectionPort(
                    href = '', 
                    id = '', 
                    link_status = '', 
                    name = '', 
                    organization = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    role = 'primary', 
                    speed = 56, 
                    status = 'requested', 
                    switch_id = '', 
                    virtual_circuits = [
                        null
                        ], ),
                project = equinix.services.metalv1.models.project.Project(
                    backend_transfer_enabled = True, 
                    bgp_config = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    customdata = equinix.services.metalv1.models.customdata.customdata(), 
                    devices = [
                        equinix.services.metalv1.models.href.Href(
                            href = '', )
                        ], 
                    href = '', 
                    id = '', 
                    invitations = [
                        
                        ], 
                    max_devices = equinix.services.metalv1.models.max_devices.max_devices(), 
                    members = [
                        
                        ], 
                    memberships = [
                        
                        ], 
                    name = '0', 
                    network_status = equinix.services.metalv1.models.network_status.network_status(), 
                    organization = , 
                    payment_method = , 
                    ssh_keys = [
                        
                        ], 
                    tags = [
                        ''
                        ], 
                    type = 'default', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    volumes = [
                        
                        ], ),
                provider_connection_id = 'dxcon-fggxx63k',
                speed = 56,
                status = 'pending',
                tags = [
                    ''
                    ],
                type = 'vlan',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                virtual_network = equinix.services.metalv1.models.href.Href(
                    href = '', ),
                vnid = 56
            )
        else:
            return VlanVirtualCircuit(
        )
        """

    def testVlanVirtualCircuit(self):
        """Test VlanVirtualCircuit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
