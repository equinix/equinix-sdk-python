# coding: utf-8

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from equinix.services.metalv1.models.bgp_dynamic_neighbor import BgpDynamicNeighbor

class TestBgpDynamicNeighbor(unittest.TestCase):
    """BgpDynamicNeighbor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BgpDynamicNeighbor:
        """Test BgpDynamicNeighbor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BgpDynamicNeighbor`
        """
        model = BgpDynamicNeighbor()
        if include_optional:
            return BgpDynamicNeighbor(
                bgp_neighbor_asn = 12345,
                bgp_neighbor_range = '192.168.1.0/25',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = equinix.services.metalv1.models.user_limited.UserLimited(
                    avatar_thumb_url = '', 
                    avatar_url = '', 
                    full_name = '', 
                    href = '', 
                    id = '', ),
                href = '/bgp-dynamic-neighbors/aea82f16-57ec-412c-9523-b7f2b27635b2',
                id = 'aea82f16-57ec-412c-9523-b7f2b27635b2',
                metal_gateway = equinix.services.metalv1.models.vrf_metal_gateway.VrfMetalGateway(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = equinix.services.metalv1.models.href.Href(
                        href = '', ), 
                    href = '', 
                    id = '', 
                    ip_reservation = equinix.services.metalv1.models.vrf_ip_reservation.VrfIpReservation(
                        address = '', 
                        address_family = 56, 
                        bill = True, 
                        cidr = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customdata = equinix.services.metalv1.models.customdata.customdata(), 
                        details = '', 
                        gateway = '', 
                        href = '', 
                        id = '', 
                        manageable = True, 
                        management = True, 
                        metal_gateway = equinix.services.metalv1.models.metal_gateway_lite.MetalGatewayLite(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            gateway_address = '10.1.2.1/27', 
                            href = '', 
                            id = '', 
                            state = 'ready', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            vlan = 1001, ), 
                        metro = equinix.services.metalv1.models.metro.Metro(
                            code = '', 
                            country = '', 
                            href = '', 
                            id = '', 
                            name = '', ), 
                        netmask = '', 
                        network = '', 
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
                        project_lite = equinix.services.metalv1.models.project.Project(
                            backend_transfer_enabled = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            customdata = equinix.services.metalv1.models.customdata.customdata(), 
                            href = '', 
                            id = '', 
                            max_devices = equinix.services.metalv1.models.max_devices.max_devices(), 
                            name = '0', 
                            network_status = equinix.services.metalv1.models.network_status.network_status(), 
                            type = 'default', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            url = '', ), 
                        public = True, 
                        state = '', 
                        tags = [
                            ''
                            ], 
                        type = 'vrf', 
                        vrf = equinix.services.metalv1.models.vrf.Vrf(
                            bgp_dynamic_neighbors_bfd_enabled = True, 
                            bgp_dynamic_neighbors_enabled = True, 
                            bgp_dynamic_neighbors_export_route_map = True, 
                            bill = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            description = '', 
                            href = '', 
                            id = '', 
                            ip_ranges = [
                                ''
                                ], 
                            local_asn = 65000, 
                            name = '', 
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
                                        role = 'primary', 
                                        speed = 56, 
                                        status = 'requested', 
                                        switch_id = '', ), 
                                    speed = 56, 
                                    status = 'pending', 
                                    subnet = '12.0.0.0/30', 
                                    subnet_ipv6 = '2604:1380:4641:a00::4/126', 
                                    type = 'vrf', 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    vrf = equinix.services.metalv1.models.vrf.Vrf(
                                        bgp_dynamic_neighbors_bfd_enabled = True, 
                                        bgp_dynamic_neighbors_enabled = True, 
                                        bgp_dynamic_neighbors_export_route_map = True, 
                                        bill = True, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', 
                                        href = '', 
                                        id = '', 
                                        local_asn = 65000, 
                                        name = '', 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                                ], ), ), 
                    project = , 
                    state = 'ready', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    virtual_network = equinix.services.metalv1.models.virtual_network.VirtualNetwork(
                        assigned_to = , 
                        assigned_to_virtual_circuit = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        description = '', 
                        facility = , 
                        href = '', 
                        id = '', 
                        instances = [
                            equinix.services.metalv1.models.device.Device(
                                actions = [
                                    equinix.services.metalv1.models.device_actions_inner.Device_actions_inner(
                                        href = '', 
                                        name = '', 
                                        type = '', )
                                    ], 
                                always_pxe = True, 
                                billing_cycle = '', 
                                bonding_mode = 56, 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                customdata = { }, 
                                description = '', 
                                firmware_set_id = '', 
                                hardware_reservation = equinix.services.metalv1.models.hardware_reservation.HardwareReservation(
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    custom_rate = 1050.5, 
                                    device = equinix.services.metalv1.models.device.Device(
                                        always_pxe = True, 
                                        billing_cycle = '', 
                                        bonding_mode = 56, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', 
                                        firmware_set_id = '', 
                                        hostname = '', 
                                        href = '', 
                                        id = '', 
                                        image_url = '', 
                                        ip_addresses = [
                                            equinix.services.metalv1.models.ip_assignment.IPAssignment(
                                                address = '', 
                                                address_family = 56, 
                                                assigned_to = , 
                                                cidr = 56, 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                enabled = True, 
                                                gateway = '', 
                                                global_ip = True, 
                                                href = '', 
                                                id = '', 
                                                manageable = True, 
                                                management = True, 
                                                netmask = '', 
                                                network = '', 
                                                next_hop = '', 
                                                parent_block = equinix.services.metalv1.models.parent_block.ParentBlock(
                                                    cidr = 56, 
                                                    href = '', 
                                                    netmask = '', 
                                                    network = '', ), 
                                                public = True, 
                                                state = 'pending', )
                                            ], 
                                        ipxe_script_url = '', 
                                        iqn = '', 
                                        locked = True, 
                                        network_frozen = True, 
                                        network_ports = [
                                            equinix.services.metalv1.models.port.Port(
                                                bond = equinix.services.metalv1.models.bond_port_data.BondPortData(
                                                    href = '', 
                                                    id = '', 
                                                    name = '', ), 
                                                data = equinix.services.metalv1.models.port_data.PortData(
                                                    bonded = True, 
                                                    href = '', 
                                                    mac = '', ), 
                                                disbond_operation_supported = True, 
                                                href = '', 
                                                id = '', 
                                                name = 'bond0', 
                                                native_virtual_network = equinix.services.metalv1.models.virtual_network.VirtualNetwork(
                                                    assigned_to_virtual_circuit = True, 
                                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    description = '', 
                                                    href = '', 
                                                    id = '', 
                                                    metal_gateways = [
                                                        equinix.services.metalv1.models.metal_gateway_lite.MetalGatewayLite(
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            gateway_address = '10.1.2.1/27', 
                                                            href = '', 
                                                            id = '', 
                                                            state = 'ready', 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            vlan = 1001, )
                                                        ], 
                                                    metro_code = '', 
                                                    vxlan = 56, ), 
                                                network_type = 'layer2-bonded', 
                                                type = 'NetworkPort', 
                                                virtual_networks = [
                                                    
                                                    ], )
                                            ], 
                                        operating_system = equinix.services.metalv1.models.operating_system.OperatingSystem(
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
                                            version = '', ), 
                                        plan = equinix.services.metalv1.models.plan.Plan(
                                            available_in = [
                                                equinix.services.metalv1.models.plan_available_in_inner.Plan_available_in_inner(
                                                    href = '', 
                                                    price = equinix.services.metalv1.models.plan_available_in_inner_price.Plan_available_in_inner_price(
                                                        hour = 1.23, 
                                                        href = '', ), )
                                                ], 
                                            available_in_metros = [
                                                equinix.services.metalv1.models.plan_available_in_metros_inner.Plan_available_in_metros_inner(
                                                    href = '', )
                                                ], 
                                            categories = [
                                                ''
                                                ], 
                                            class = 'm3.large.x86', 
                                            deployment_types = [
                                                'on_demand'
                                                ], 
                                            description = '', 
                                            href = '', 
                                            id = '', 
                                            legacy = True, 
                                            line = '', 
                                            name = '', 
                                            pricing = equinix.services.metalv1.models.pricing.pricing(), 
                                            slug = 'm3.large.x86', 
                                            specs = equinix.services.metalv1.models.plan_specs.Plan_specs(
                                                cpus = [
                                                    equinix.services.metalv1.models.plan_specs_cpus_inner.Plan_specs_cpus_inner(
                                                        count = 56, 
                                                        href = '', 
                                                        type = '', )
                                                    ], 
                                                drives = [
                                                    equinix.services.metalv1.models.plan_specs_drives_inner.Plan_specs_drives_inner(
                                                        category = '', 
                                                        count = 56, 
                                                        href = '', 
                                                        size = '3.84TB', 
                                                        type = '', )
                                                    ], 
                                                features = equinix.services.metalv1.models.plan_specs_features.Plan_specs_features(
                                                    href = '', 
                                                    raid = True, 
                                                    txt = True, 
                                                    uefi = True, ), 
                                                href = '', 
                                                memory = equinix.services.metalv1.models.plan_specs_memory.Plan_specs_memory(
                                                    href = '', 
                                                    total = '', ), 
                                                nics = [
                                                    equinix.services.metalv1.models.plan_specs_nics_inner.Plan_specs_nics_inner(
                                                        count = 2, 
                                                        href = '', 
                                                        type = '', )
                                                    ], ), 
                                            type = 'standard', ), 
                                        provisioning_events = [
                                            equinix.services.metalv1.models.event.Event(
                                                body = '', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                href = '', 
                                                id = '', 
                                                interpolated = '', 
                                                ip = '', 
                                                modified_by = equinix.services.metalv1.models.modified_by.modified_by(), 
                                                relationships = [
                                                    
                                                    ], 
                                                state = '', 
                                                type = '', )
                                            ], 
                                        provisioning_percentage = 1.337, 
                                        root_password = '', 
                                        short_id = '', 
                                        sos = '', 
                                        spot_instance = True, 
                                        spot_price_max = 1.337, 
                                        state = 'queued', 
                                        storage = equinix.services.metalv1.models.storage.Storage(
                                            disks = [
                                                equinix.services.metalv1.models.disk.Disk(
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
                                                    href = '', 
                                                    level = '', 
                                                    name = '', )
                                                ], ), 
                                        switch_uuid = '', 
                                        termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        user = '', 
                                        userdata = '', ), 
                                    href = '', 
                                    id = '', 
                                    need_of_service = True, 
                                    plan = equinix.services.metalv1.models.plan.Plan(
                                        class = 'm3.large.x86', 
                                        description = '', 
                                        href = '', 
                                        id = '', 
                                        legacy = True, 
                                        line = '', 
                                        name = '', 
                                        pricing = equinix.services.metalv1.models.pricing.pricing(), 
                                        slug = 'm3.large.x86', 
                                        type = 'standard', ), 
                                    provisionable = True, 
                                    short_id = '', 
                                    spare = True, 
                                    switch_uuid = '', 
                                    termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                hostname = '', 
                                href = '', 
                                id = '', 
                                image_url = '', 
                                ip_addresses = [
                                    equinix.services.metalv1.models.ip_assignment.IPAssignment(
                                        address = '', 
                                        address_family = 56, 
                                        assigned_to = , 
                                        cidr = 56, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        enabled = True, 
                                        gateway = '', 
                                        global_ip = True, 
                                        href = '', 
                                        id = '', 
                                        manageable = True, 
                                        management = True, 
                                        netmask = '', 
                                        network = '', 
                                        next_hop = '', 
                                        public = True, 
                                        state = 'pending', )
                                    ], 
                                ipxe_script_url = '', 
                                iqn = '', 
                                locked = True, 
                                network_frozen = True, 
                                network_ports = [
                                    equinix.services.metalv1.models.port.Port(
                                        disbond_operation_supported = True, 
                                        href = '', 
                                        id = '', 
                                        name = 'bond0', 
                                        network_type = 'layer2-bonded', 
                                        type = 'NetworkPort', )
                                    ], 
                                operating_system = equinix.services.metalv1.models.operating_system.OperatingSystem(
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
                                    release_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                    release_notes = '', 
                                    slug = '', 
                                    version = '', ), 
                                plan = , 
                                provisioning_events = [
                                    equinix.services.metalv1.models.event.Event(
                                        body = '', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        href = '', 
                                        id = '', 
                                        interpolated = '', 
                                        ip = '', 
                                        modified_by = equinix.services.metalv1.models.modified_by.modified_by(), 
                                        state = '', 
                                        type = '', )
                                    ], 
                                provisioning_percentage = 1.337, 
                                root_password = '', 
                                short_id = '', 
                                sos = '', 
                                spot_instance = True, 
                                spot_price_max = 1.337, 
                                state = 'queued', 
                                storage = equinix.services.metalv1.models.storage.Storage(
                                    href = '', ), 
                                switch_uuid = '', 
                                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                user = '', 
                                userdata = '', )
                            ], 
                        metal_gateways = [
                            
                            ], 
                        metro_code = '', 
                        vxlan = 56, ), 
                    vrf = , ),
                state = 'active',
                tags = [
                    ''
                    ],
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BgpDynamicNeighbor(
        )
        """

    def testBgpDynamicNeighbor(self):
        """Test BgpDynamicNeighbor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
