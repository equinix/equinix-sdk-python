# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.vrf import Vrf

class TestVrf(unittest.TestCase):
    """Vrf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Vrf:
        """Test Vrf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Vrf`
        """
        model = Vrf()
        if include_optional:
            return Vrf(
                bgp_dynamic_neighbors_bfd_enabled = True,
                bgp_dynamic_neighbors_enabled = True,
                bgp_dynamic_neighbors_export_route_map = True,
                bill = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = equinix.services.metalv1.models.user.User(
                    avatar_thumb_url = '', 
                    avatar_url = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    customdata = equinix.services.metalv1.models.customdata.customdata(), 
                    default_organization_id = '', 
                    default_project_id = '', 
                    email = '', 
                    emails = [
                        equinix.services.metalv1.models.href.Href(
                            href = '', )
                        ], 
                    first_name = '', 
                    fraud_score = '', 
                    full_name = '', 
                    href = '', 
                    id = '', 
                    last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_name = '', 
                    max_organizations = 56, 
                    max_projects = 56, 
                    phone_number = '', 
                    short_id = '', 
                    timezone = '', 
                    two_factor_auth = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                description = '',
                href = '',
                id = '',
                ip_ranges = [
                    ''
                    ],
                local_asn = 65000,
                metro = equinix.services.metalv1.models.metro.Metro(
                    code = '', 
                    country = '', 
                    href = '', 
                    id = '', 
                    name = '', ),
                name = '',
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
                tags = [
                    ''
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                virtual_circuits = [
                    equinix.services.metalv1.models.vrf_virtual_circuit.VrfVirtualCircuit(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customer_ip = '12.0.0.2', 
                        customer_ipv6 = '2604:1380:4641:a00::6', 
                        description = '', 
                        href = '', 
                        id = '', 
                        md5 = '', 
                        metal_ip = '12.0.0.1', 
                        metal_ipv6 = '2604:1380:4641:a00::6', 
                        name = '', 
                        nni_vlan = 56, 
                        peer_asn = 65000, 
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
                            switch_id = '', ), 
                        project = equinix.services.metalv1.models.project.Project(
                            backend_transfer_enabled = True, 
                            bgp_config = equinix.services.metalv1.models.href.Href(
                                href = '', ), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            customdata = equinix.services.metalv1.models.customdata.customdata(), 
                            devices = [
                                
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
                        speed = 56, 
                        status = 'pending', 
                        subnet = '12.0.0.0/30', 
                        subnet_ipv6 = '2604:1380:4641:a00::4/126', 
                        tags = [
                            ''
                            ], 
                        type = 'vrf', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        vrf = equinix.services.metalv1.models.vrf.Vrf(
                            bgp_dynamic_neighbors_bfd_enabled = True, 
                            bgp_dynamic_neighbors_enabled = True, 
                            bgp_dynamic_neighbors_export_route_map = True, 
                            bill = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            created_by = equinix.services.metalv1.models.user.User(
                                avatar_thumb_url = '', 
                                avatar_url = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                customdata = equinix.services.metalv1.models.customdata.customdata(), 
                                default_organization_id = '', 
                                default_project_id = '', 
                                email = '', 
                                emails = [
                                    
                                    ], 
                                first_name = '', 
                                fraud_score = '', 
                                full_name = '', 
                                href = '', 
                                id = '', 
                                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_name = '', 
                                max_organizations = 56, 
                                max_projects = 56, 
                                phone_number = '', 
                                short_id = '', 
                                timezone = '', 
                                two_factor_auth = '', 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            description = '', 
                            href = '', 
                            id = '', 
                            ip_ranges = [
                                ''
                                ], 
                            local_asn = 65000, 
                            metro = equinix.services.metalv1.models.metro.Metro(
                                code = '', 
                                country = '', 
                                href = '', 
                                id = '', 
                                name = '', ), 
                            name = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                    ]
            )
        else:
            return Vrf(
        )
        """

    def testVrf(self):
        """Test Vrf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
