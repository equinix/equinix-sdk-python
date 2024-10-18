# coding: utf-8

# flake8: noqa

"""
    Metal API

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.6.0"

# import apis into sdk package
from equinix.services.metalv1.api.authentication_api import AuthenticationApi
from equinix.services.metalv1.api.bgp_api import BGPApi
from equinix.services.metalv1.api.batches_api import BatchesApi
from equinix.services.metalv1.api.capacity_api import CapacityApi
from equinix.services.metalv1.api.console_log_details_api import ConsoleLogDetailsApi
from equinix.services.metalv1.api.devices_api import DevicesApi
from equinix.services.metalv1.api.emails_api import EmailsApi
from equinix.services.metalv1.api.events_api import EventsApi
from equinix.services.metalv1.api.facilities_api import FacilitiesApi
from equinix.services.metalv1.api.firmware_sets_api import FirmwareSetsApi
from equinix.services.metalv1.api.hardware_reservations_api import HardwareReservationsApi
from equinix.services.metalv1.api.ip_addresses_api import IPAddressesApi
from equinix.services.metalv1.api.incidents_api import IncidentsApi
from equinix.services.metalv1.api.interconnections_api import InterconnectionsApi
from equinix.services.metalv1.api.invitations_api import InvitationsApi
from equinix.services.metalv1.api.invoices_api import InvoicesApi
from equinix.services.metalv1.api.licenses_api import LicensesApi
from equinix.services.metalv1.api.memberships_api import MembershipsApi
from equinix.services.metalv1.api.metal_gateways_api import MetalGatewaysApi
from equinix.services.metalv1.api.metros_api import MetrosApi
from equinix.services.metalv1.api.operating_systems_api import OperatingSystemsApi
from equinix.services.metalv1.api.organizations_api import OrganizationsApi
from equinix.services.metalv1.api.password_reset_tokens_api import PasswordResetTokensApi
from equinix.services.metalv1.api.payment_methods_api import PaymentMethodsApi
from equinix.services.metalv1.api.plans_api import PlansApi
from equinix.services.metalv1.api.ports_api import PortsApi
from equinix.services.metalv1.api.projects_api import ProjectsApi
from equinix.services.metalv1.api.roles_api import RolesApi
from equinix.services.metalv1.api.ssh_keys_api import SSHKeysApi
from equinix.services.metalv1.api.self_service_reservations_api import SelfServiceReservationsApi
from equinix.services.metalv1.api.spot_market_api import SpotMarketApi
from equinix.services.metalv1.api.support_request_api import SupportRequestApi
from equinix.services.metalv1.api.transfer_requests_api import TransferRequestsApi
from equinix.services.metalv1.api.two_factor_auth_api import TwoFactorAuthApi
from equinix.services.metalv1.api.usages_api import UsagesApi
from equinix.services.metalv1.api.user_verification_tokens_api import UserVerificationTokensApi
from equinix.services.metalv1.api.userdata_api import UserdataApi
from equinix.services.metalv1.api.users_api import UsersApi
from equinix.services.metalv1.api.vlans_api import VLANsApi
from equinix.services.metalv1.api.vrfs_api import VRFsApi

# import ApiClient
from equinix.services.metalv1.api_response import ApiResponse
from equinix.services.metalv1.api_client import ApiClient
from equinix.services.metalv1.configuration import Configuration
from equinix.services.metalv1.exceptions import OpenApiException
from equinix.services.metalv1.exceptions import ApiTypeError
from equinix.services.metalv1.exceptions import ApiValueError
from equinix.services.metalv1.exceptions import ApiKeyError
from equinix.services.metalv1.exceptions import ApiAttributeError
from equinix.services.metalv1.exceptions import ApiException

# import models into sdk package
from equinix.services.metalv1.models.aws_fabric_provider import AWSFabricProvider
from equinix.services.metalv1.models.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from equinix.services.metalv1.models.address import Address
from equinix.services.metalv1.models.attribute import Attribute
from equinix.services.metalv1.models.attribute_data import AttributeData
from equinix.services.metalv1.models.auth_token import AuthToken
from equinix.services.metalv1.models.auth_token_input import AuthTokenInput
from equinix.services.metalv1.models.auth_token_list import AuthTokenList
from equinix.services.metalv1.models.auth_token_project import AuthTokenProject
from equinix.services.metalv1.models.auth_token_user import AuthTokenUser
from equinix.services.metalv1.models.bgp_session_input import BGPSessionInput
from equinix.services.metalv1.models.batch import Batch
from equinix.services.metalv1.models.batches_list import BatchesList
from equinix.services.metalv1.models.bgp_config import BgpConfig
from equinix.services.metalv1.models.bgp_config_request_input import BgpConfigRequestInput
from equinix.services.metalv1.models.bgp_dynamic_neighbor import BgpDynamicNeighbor
from equinix.services.metalv1.models.bgp_dynamic_neighbor_create_input import BgpDynamicNeighborCreateInput
from equinix.services.metalv1.models.bgp_dynamic_neighbor_list import BgpDynamicNeighborList
from equinix.services.metalv1.models.bgp_neighbor_data import BgpNeighborData
from equinix.services.metalv1.models.bgp_route import BgpRoute
from equinix.services.metalv1.models.bgp_session import BgpSession
from equinix.services.metalv1.models.bgp_session_list import BgpSessionList
from equinix.services.metalv1.models.bgp_session_neighbors import BgpSessionNeighbors
from equinix.services.metalv1.models.bond_port_data import BondPortData
from equinix.services.metalv1.models.capacity_check_per_facility_info import CapacityCheckPerFacilityInfo
from equinix.services.metalv1.models.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from equinix.services.metalv1.models.capacity_check_per_metro_info import CapacityCheckPerMetroInfo
from equinix.services.metalv1.models.capacity_check_per_metro_list import CapacityCheckPerMetroList
from equinix.services.metalv1.models.capacity_input import CapacityInput
from equinix.services.metalv1.models.capacity_level_per_baremetal import CapacityLevelPerBaremetal
from equinix.services.metalv1.models.capacity_list import CapacityList
from equinix.services.metalv1.models.component import Component
from equinix.services.metalv1.models.coordinates import Coordinates
from equinix.services.metalv1.models.create_device_request import CreateDeviceRequest
from equinix.services.metalv1.models.create_email_input import CreateEmailInput
from equinix.services.metalv1.models.create_metal_gateway_request import CreateMetalGatewayRequest
from equinix.services.metalv1.models.create_organization_interconnection_request import CreateOrganizationInterconnectionRequest
from equinix.services.metalv1.models.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from equinix.services.metalv1.models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
from equinix.services.metalv1.models.dedicated_port_create_input import DedicatedPortCreateInput
from equinix.services.metalv1.models.device import Device
from equinix.services.metalv1.models.device_action_input import DeviceActionInput
from equinix.services.metalv1.models.device_actions_inner import DeviceActionsInner
from equinix.services.metalv1.models.device_create_in_facility_input import DeviceCreateInFacilityInput
from equinix.services.metalv1.models.device_create_in_metro_input import DeviceCreateInMetroInput
from equinix.services.metalv1.models.device_create_input import DeviceCreateInput
from equinix.services.metalv1.models.device_created_by import DeviceCreatedBy
from equinix.services.metalv1.models.device_health_rollup import DeviceHealthRollup
from equinix.services.metalv1.models.device_list import DeviceList
from equinix.services.metalv1.models.device_metro import DeviceMetro
from equinix.services.metalv1.models.device_project_lite import DeviceProjectLite
from equinix.services.metalv1.models.device_update_input import DeviceUpdateInput
from equinix.services.metalv1.models.device_usage import DeviceUsage
from equinix.services.metalv1.models.device_usage_list import DeviceUsageList
from equinix.services.metalv1.models.disk import Disk
from equinix.services.metalv1.models.email import Email
from equinix.services.metalv1.models.email_input import EmailInput
from equinix.services.metalv1.models.entitlement import Entitlement
from equinix.services.metalv1.models.error import Error
from equinix.services.metalv1.models.event import Event
from equinix.services.metalv1.models.event_list import EventList
from equinix.services.metalv1.models.fabric_service_token import FabricServiceToken
from equinix.services.metalv1.models.facility import Facility
from equinix.services.metalv1.models.facility_input import FacilityInput
from equinix.services.metalv1.models.facility_input_facility import FacilityInputFacility
from equinix.services.metalv1.models.facility_list import FacilityList
from equinix.services.metalv1.models.filesystem import Filesystem
from equinix.services.metalv1.models.find_ip_address_by_id200_response import FindIPAddressById200Response
from equinix.services.metalv1.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
from equinix.services.metalv1.models.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from equinix.services.metalv1.models.firmware_set import FirmwareSet
from equinix.services.metalv1.models.firmware_set_list_response import FirmwareSetListResponse
from equinix.services.metalv1.models.firmware_set_response import FirmwareSetResponse
from equinix.services.metalv1.models.global_bgp_range import GlobalBgpRange
from equinix.services.metalv1.models.global_bgp_range_list import GlobalBgpRangeList
from equinix.services.metalv1.models.hardware_reservation import HardwareReservation
from equinix.services.metalv1.models.hardware_reservation_list import HardwareReservationList
from equinix.services.metalv1.models.href import Href
from equinix.services.metalv1.models.ip_address import IPAddress
from equinix.services.metalv1.models.ip_assignment import IPAssignment
from equinix.services.metalv1.models.ip_assignment_input import IPAssignmentInput
from equinix.services.metalv1.models.ip_assignment_list import IPAssignmentList
from equinix.services.metalv1.models.ip_assignment_metro import IPAssignmentMetro
from equinix.services.metalv1.models.ip_assignment_update_input import IPAssignmentUpdateInput
from equinix.services.metalv1.models.ip_availabilities_list import IPAvailabilitiesList
from equinix.services.metalv1.models.ip_reservation import IPReservation
from equinix.services.metalv1.models.ip_reservation_facility import IPReservationFacility
from equinix.services.metalv1.models.ip_reservation_list import IPReservationList
from equinix.services.metalv1.models.ip_reservation_list_ip_addresses_inner import IPReservationListIpAddressesInner
from equinix.services.metalv1.models.ip_reservation_metro import IPReservationMetro
from equinix.services.metalv1.models.ip_reservation_request_input import IPReservationRequestInput
from equinix.services.metalv1.models.instances_batch_create_input import InstancesBatchCreateInput
from equinix.services.metalv1.models.instances_batch_create_input_batches_inner import InstancesBatchCreateInputBatchesInner
from equinix.services.metalv1.models.interconnection import Interconnection
from equinix.services.metalv1.models.interconnection_fabric_provider import InterconnectionFabricProvider
from equinix.services.metalv1.models.interconnection_list import InterconnectionList
from equinix.services.metalv1.models.interconnection_metro_list import InterconnectionMetroList
from equinix.services.metalv1.models.interconnection_metro_list_metros_inner import InterconnectionMetroListMetrosInner
from equinix.services.metalv1.models.interconnection_metro_list_metros_inner_all_of_providers_inner import InterconnectionMetroListMetrosInnerAllOfProvidersInner
from equinix.services.metalv1.models.interconnection_port import InterconnectionPort
from equinix.services.metalv1.models.interconnection_port_list import InterconnectionPortList
from equinix.services.metalv1.models.interconnection_pricing_list import InterconnectionPricingList
from equinix.services.metalv1.models.interconnection_pricing_list_provider_pricing_inner import InterconnectionPricingListProviderPricingInner
from equinix.services.metalv1.models.interconnection_pricing_list_provider_pricing_inner_tiers_inner import InterconnectionPricingListProviderPricingInnerTiersInner
from equinix.services.metalv1.models.interconnection_update_input import InterconnectionUpdateInput
from equinix.services.metalv1.models.invitation import Invitation
from equinix.services.metalv1.models.invitation_input import InvitationInput
from equinix.services.metalv1.models.invitation_list import InvitationList
from equinix.services.metalv1.models.invoice import Invoice
from equinix.services.metalv1.models.invoice_list import InvoiceList
from equinix.services.metalv1.models.license import License
from equinix.services.metalv1.models.license_create_input import LicenseCreateInput
from equinix.services.metalv1.models.license_list import LicenseList
from equinix.services.metalv1.models.license_update_input import LicenseUpdateInput
from equinix.services.metalv1.models.line_item import LineItem
from equinix.services.metalv1.models.line_item_adjustment import LineItemAdjustment
from equinix.services.metalv1.models.member import Member
from equinix.services.metalv1.models.member_list import MemberList
from equinix.services.metalv1.models.member_update_input import MemberUpdateInput
from equinix.services.metalv1.models.membership import Membership
from equinix.services.metalv1.models.membership_input import MembershipInput
from equinix.services.metalv1.models.membership_list import MembershipList
from equinix.services.metalv1.models.meta import Meta
from equinix.services.metalv1.models.metadata import Metadata
from equinix.services.metalv1.models.metadata_network import MetadataNetwork
from equinix.services.metalv1.models.metadata_network_network import MetadataNetworkNetwork
from equinix.services.metalv1.models.metadata_network_network_bonding import MetadataNetworkNetworkBonding
from equinix.services.metalv1.models.metal_gateway import MetalGateway
from equinix.services.metalv1.models.metal_gateway_create_input import MetalGatewayCreateInput
from equinix.services.metalv1.models.metal_gateway_elastic_ip_create_input import MetalGatewayElasticIpCreateInput
from equinix.services.metalv1.models.metal_gateway_list import MetalGatewayList
from equinix.services.metalv1.models.metal_gateway_list_metal_gateways_inner import MetalGatewayListMetalGatewaysInner
from equinix.services.metalv1.models.metal_gateway_lite import MetalGatewayLite
from equinix.services.metalv1.models.metro import Metro
from equinix.services.metalv1.models.metro_input import MetroInput
from equinix.services.metalv1.models.metro_list import MetroList
from equinix.services.metalv1.models.mount import Mount
from equinix.services.metalv1.models.move_hardware_reservation_request import MoveHardwareReservationRequest
from equinix.services.metalv1.models.new_password import NewPassword
from equinix.services.metalv1.models.operating_system import OperatingSystem
from equinix.services.metalv1.models.operating_system_list import OperatingSystemList
from equinix.services.metalv1.models.organization import Organization
from equinix.services.metalv1.models.organization_input import OrganizationInput
from equinix.services.metalv1.models.organization_list import OrganizationList
from equinix.services.metalv1.models.parent_block import ParentBlock
from equinix.services.metalv1.models.partition import Partition
from equinix.services.metalv1.models.payment_method import PaymentMethod
from equinix.services.metalv1.models.payment_method_billing_address import PaymentMethodBillingAddress
from equinix.services.metalv1.models.payment_method_create_input import PaymentMethodCreateInput
from equinix.services.metalv1.models.payment_method_list import PaymentMethodList
from equinix.services.metalv1.models.payment_method_update_input import PaymentMethodUpdateInput
from equinix.services.metalv1.models.plan import Plan
from equinix.services.metalv1.models.plan_available_in_inner import PlanAvailableInInner
from equinix.services.metalv1.models.plan_available_in_inner_price import PlanAvailableInInnerPrice
from equinix.services.metalv1.models.plan_available_in_metros_inner import PlanAvailableInMetrosInner
from equinix.services.metalv1.models.plan_id_name import PlanIdName
from equinix.services.metalv1.models.plan_list import PlanList
from equinix.services.metalv1.models.plan_specs import PlanSpecs
from equinix.services.metalv1.models.plan_specs_cpus_inner import PlanSpecsCpusInner
from equinix.services.metalv1.models.plan_specs_drives_inner import PlanSpecsDrivesInner
from equinix.services.metalv1.models.plan_specs_features import PlanSpecsFeatures
from equinix.services.metalv1.models.plan_specs_memory import PlanSpecsMemory
from equinix.services.metalv1.models.plan_specs_nics_inner import PlanSpecsNicsInner
from equinix.services.metalv1.models.port import Port
from equinix.services.metalv1.models.port_assign_input import PortAssignInput
from equinix.services.metalv1.models.port_convert_layer3_input import PortConvertLayer3Input
from equinix.services.metalv1.models.port_convert_layer3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner
from equinix.services.metalv1.models.port_data import PortData
from equinix.services.metalv1.models.port_vlan_assignment import PortVlanAssignment
from equinix.services.metalv1.models.port_vlan_assignment_batch import PortVlanAssignmentBatch
from equinix.services.metalv1.models.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput
from equinix.services.metalv1.models.port_vlan_assignment_batch_create_input_vlan_assignments_inner import PortVlanAssignmentBatchCreateInputVlanAssignmentsInner
from equinix.services.metalv1.models.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList
from equinix.services.metalv1.models.port_vlan_assignment_batch_vlan_assignments_inner import PortVlanAssignmentBatchVlanAssignmentsInner
from equinix.services.metalv1.models.port_vlan_assignment_list import PortVlanAssignmentList
from equinix.services.metalv1.models.project import Project
from equinix.services.metalv1.models.project_create_from_root_input import ProjectCreateFromRootInput
from equinix.services.metalv1.models.project_create_input import ProjectCreateInput
from equinix.services.metalv1.models.project_id_name import ProjectIdName
from equinix.services.metalv1.models.project_list import ProjectList
from equinix.services.metalv1.models.project_update_input import ProjectUpdateInput
from equinix.services.metalv1.models.project_usage import ProjectUsage
from equinix.services.metalv1.models.project_usage_list import ProjectUsageList
from equinix.services.metalv1.models.raid import Raid
from equinix.services.metalv1.models.request_ip_reservation201_response import RequestIPReservation201Response
from equinix.services.metalv1.models.request_ip_reservation_request import RequestIPReservationRequest
from equinix.services.metalv1.models.role import Role
from equinix.services.metalv1.models.role_list import RoleList
from equinix.services.metalv1.models.role_list_roles_inner import RoleListRolesInner
from equinix.services.metalv1.models.ssh_key import SSHKey
from equinix.services.metalv1.models.ssh_key_create_input import SSHKeyCreateInput
from equinix.services.metalv1.models.ssh_key_input import SSHKeyInput
from equinix.services.metalv1.models.ssh_key_list import SSHKeyList
from equinix.services.metalv1.models.self_service_reservation_item_request import SelfServiceReservationItemRequest
from equinix.services.metalv1.models.self_service_reservation_item_response import SelfServiceReservationItemResponse
from equinix.services.metalv1.models.self_service_reservation_list import SelfServiceReservationList
from equinix.services.metalv1.models.self_service_reservation_response import SelfServiceReservationResponse
from equinix.services.metalv1.models.server_info import ServerInfo
from equinix.services.metalv1.models.shared_port_vc_vlan_create_input import SharedPortVCVlanCreateInput
from equinix.services.metalv1.models.spot_market_prices_list import SpotMarketPricesList
from equinix.services.metalv1.models.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from equinix.services.metalv1.models.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport
from equinix.services.metalv1.models.spot_market_request import SpotMarketRequest
from equinix.services.metalv1.models.spot_market_request_create_input import SpotMarketRequestCreateInput
from equinix.services.metalv1.models.spot_market_request_create_input_instance_parameters import SpotMarketRequestCreateInputInstanceParameters
from equinix.services.metalv1.models.spot_market_request_list import SpotMarketRequestList
from equinix.services.metalv1.models.spot_market_request_metro import SpotMarketRequestMetro
from equinix.services.metalv1.models.spot_prices_datapoints import SpotPricesDatapoints
from equinix.services.metalv1.models.spot_prices_history_report import SpotPricesHistoryReport
from equinix.services.metalv1.models.spot_prices_per_baremetal import SpotPricesPerBaremetal
from equinix.services.metalv1.models.spot_prices_per_facility import SpotPricesPerFacility
from equinix.services.metalv1.models.spot_prices_per_new_facility import SpotPricesPerNewFacility
from equinix.services.metalv1.models.spot_prices_report import SpotPricesReport
from equinix.services.metalv1.models.storage import Storage
from equinix.services.metalv1.models.support_request_input import SupportRequestInput
from equinix.services.metalv1.models.transfer_request import TransferRequest
from equinix.services.metalv1.models.transfer_request_input import TransferRequestInput
from equinix.services.metalv1.models.transfer_request_list import TransferRequestList
from equinix.services.metalv1.models.update_email_input import UpdateEmailInput
from equinix.services.metalv1.models.user import User
from equinix.services.metalv1.models.user_create_input import UserCreateInput
from equinix.services.metalv1.models.user_limited import UserLimited
from equinix.services.metalv1.models.user_list import UserList
from equinix.services.metalv1.models.user_lite import UserLite
from equinix.services.metalv1.models.user_update_input import UserUpdateInput
from equinix.services.metalv1.models.userdata import Userdata
from equinix.services.metalv1.models.verify_email import VerifyEmail
from equinix.services.metalv1.models.virtual_circuit import VirtualCircuit
from equinix.services.metalv1.models.virtual_circuit_create_input import VirtualCircuitCreateInput
from equinix.services.metalv1.models.virtual_circuit_list import VirtualCircuitList
from equinix.services.metalv1.models.virtual_circuit_update_input import VirtualCircuitUpdateInput
from equinix.services.metalv1.models.virtual_network import VirtualNetwork
from equinix.services.metalv1.models.virtual_network_create_input import VirtualNetworkCreateInput
from equinix.services.metalv1.models.virtual_network_list import VirtualNetworkList
from equinix.services.metalv1.models.virtual_network_update_input import VirtualNetworkUpdateInput
from equinix.services.metalv1.models.vlan_csp_connection_create_input import VlanCSPConnectionCreateInput
from equinix.services.metalv1.models.vlan_csp_connection_create_input_fabric_provider import VlanCSPConnectionCreateInputFabricProvider
from equinix.services.metalv1.models.vlan_fabric_vc_create_input import VlanFabricVcCreateInput
from equinix.services.metalv1.models.vlan_virtual_circuit import VlanVirtualCircuit
from equinix.services.metalv1.models.vlan_virtual_circuit_create_input import VlanVirtualCircuitCreateInput
from equinix.services.metalv1.models.vlan_virtual_circuit_update_input import VlanVirtualCircuitUpdateInput
from equinix.services.metalv1.models.vrf import Vrf
from equinix.services.metalv1.models.vrf_bgp_neighbors import VrfBGPNeighbors
from equinix.services.metalv1.models.vrf_bgp_neighbors_list import VrfBGPNeighborsList
from equinix.services.metalv1.models.vrf_create_input import VrfCreateInput
from equinix.services.metalv1.models.vrf_fabric_vc_create_input import VrfFabricVcCreateInput
from equinix.services.metalv1.models.vrf_ip_reservation import VrfIpReservation
from equinix.services.metalv1.models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput
from equinix.services.metalv1.models.vrf_ip_reservation_list import VrfIpReservationList
from equinix.services.metalv1.models.vrf_learned_routes import VrfLearnedRoutes
from equinix.services.metalv1.models.vrf_learned_routes_list import VrfLearnedRoutesList
from equinix.services.metalv1.models.vrf_list import VrfList
from equinix.services.metalv1.models.vrf_metal_gateway import VrfMetalGateway
from equinix.services.metalv1.models.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput
from equinix.services.metalv1.models.vrf_route import VrfRoute
from equinix.services.metalv1.models.vrf_route_create_input import VrfRouteCreateInput
from equinix.services.metalv1.models.vrf_route_list import VrfRouteList
from equinix.services.metalv1.models.vrf_route_update_input import VrfRouteUpdateInput
from equinix.services.metalv1.models.vrf_update_input import VrfUpdateInput
from equinix.services.metalv1.models.vrf_virtual_circuit import VrfVirtualCircuit
from equinix.services.metalv1.models.vrf_virtual_circuit_create_input import VrfVirtualCircuitCreateInput
from equinix.services.metalv1.models.vrf_virtual_circuit_update_input import VrfVirtualCircuitUpdateInput
