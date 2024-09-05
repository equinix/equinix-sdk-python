# coding: utf-8

# flake8: noqa

"""
    Metal API

    # Introduction Equinix Metal provides a RESTful HTTP API which can be reached at <https://api.equinix.com/metal/v1>. This document describes the API and how to use it.  The API allows you to programmatically interact with all of your Equinix Metal resources, including devices, networks, addresses, organizations, projects, and your user account. Every feature of the Equinix Metal web interface is accessible through the API.  The API docs are generated from the Equinix Metal OpenAPI specification and are officially hosted at <https://deploy.equinix.com/developers/api/metal/>.  # Common Parameters  The Equinix Metal API uses a few methods to minimize network traffic and improve throughput. These parameters are not used in all API calls, but are used often enough to warrant their own section. Look for these parameters in the documentation for the API calls that support them.  ## Pagination  Pagination is used to limit the number of results returned in a single request. The API will return a maximum of 100 results per page. To retrieve additional results, you can use the `page` and `per_page` query parameters.  The `page` parameter is used to specify the page number. The first page is `1`. The `per_page` parameter is used to specify the number of results per page. The maximum number of results differs by resource type.  ## Sorting  Where offered, the API allows you to sort results by a specific field. To sort results use the `sort_by` query parameter with the root level field name as the value. The `sort_direction` parameter is used to specify the sort direction, either either `asc` (ascending) or `desc` (descending).  ## Filtering  Filtering is used to limit the results returned in a single request. The API supports filtering by certain fields in the response. To filter results, you can use the field as a query parameter.  For example, to filter the IP list to only return public IPv4 addresses, you can filter by the `type` field, as in the following request:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/projects/id/ips?type=public_ipv4 ```  Only IP addresses with the `type` field set to `public_ipv4` will be returned.  ## Searching  Searching is used to find matching resources using multiple field comparissons. The API supports searching in resources that define this behavior. Currently the search parameter is only available on devices, ssh_keys, api_keys and memberships endpoints.  To search resources you can use the `search` query parameter.  ## Include and Exclude  For resources that contain references to other resources, sucha as a Device that refers to the Project it resides in, the Equinix Metal API will returns `href` values (API links) to the associated resource.  ```json {   ...   \"project\": {     \"href\": \"/metal/v1/projects/f3f131c8-f302-49ef-8c44-9405022dc6dd\"   } } ```  If you're going need the project details, you can avoid a second API request.  Specify the contained `href` resources and collections that you'd like to have included in the response using the `include` query parameter.  For example:  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=projects ```  The `include` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests where `href` resources are presented.  To have multiple resources include, use a comma-separated list (e.g. `?include=emails,projects,memberships`).  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=emails,projects,memberships ```  You may also include nested associations up to three levels deep using dot notation (`?include=memberships.projects`):  ```sh curl -H 'X-Auth-Token: my_authentication_token' \\   https://api.equinix.com/metal/v1/user?include=memberships.projects ```  To exclude resources, and optimize response delivery, use the `exclude` query parameter. The `exclude` parameter is generally accepted in `GET`, `POST`, `PUT`, and `PATCH` requests for fields with nested object responses. When excluded, these fields will be replaced with an object that contains only an `href` field. 

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.11.0"

# import apis into sdk package
from equinix_metal.api.authentication_api import AuthenticationApi
from equinix_metal.api.bgp_api import BGPApi
from equinix_metal.api.batches_api import BatchesApi
from equinix_metal.api.capacity_api import CapacityApi
from equinix_metal.api.console_log_details_api import ConsoleLogDetailsApi
from equinix_metal.api.devices_api import DevicesApi
from equinix_metal.api.emails_api import EmailsApi
from equinix_metal.api.events_api import EventsApi
from equinix_metal.api.facilities_api import FacilitiesApi
from equinix_metal.api.firmware_sets_api import FirmwareSetsApi
from equinix_metal.api.hardware_reservations_api import HardwareReservationsApi
from equinix_metal.api.ip_addresses_api import IPAddressesApi
from equinix_metal.api.incidents_api import IncidentsApi
from equinix_metal.api.interconnections_api import InterconnectionsApi
from equinix_metal.api.invitations_api import InvitationsApi
from equinix_metal.api.invoices_api import InvoicesApi
from equinix_metal.api.licenses_api import LicensesApi
from equinix_metal.api.memberships_api import MembershipsApi
from equinix_metal.api.metal_gateways_api import MetalGatewaysApi
from equinix_metal.api.metros_api import MetrosApi
from equinix_metal.api.otps_api import OTPsApi
from equinix_metal.api.operating_systems_api import OperatingSystemsApi
from equinix_metal.api.organizations_api import OrganizationsApi
from equinix_metal.api.password_reset_tokens_api import PasswordResetTokensApi
from equinix_metal.api.payment_methods_api import PaymentMethodsApi
from equinix_metal.api.plans_api import PlansApi
from equinix_metal.api.ports_api import PortsApi
from equinix_metal.api.projects_api import ProjectsApi
from equinix_metal.api.ssh_keys_api import SSHKeysApi
from equinix_metal.api.self_service_reservations_api import SelfServiceReservationsApi
from equinix_metal.api.spot_market_api import SpotMarketApi
from equinix_metal.api.support_request_api import SupportRequestApi
from equinix_metal.api.transfer_requests_api import TransferRequestsApi
from equinix_metal.api.two_factor_auth_api import TwoFactorAuthApi
from equinix_metal.api.usages_api import UsagesApi
from equinix_metal.api.user_verification_tokens_api import UserVerificationTokensApi
from equinix_metal.api.userdata_api import UserdataApi
from equinix_metal.api.users_api import UsersApi
from equinix_metal.api.vlans_api import VLANsApi
from equinix_metal.api.vrfs_api import VRFsApi

# import ApiClient
from equinix_metal.api_response import ApiResponse
from equinix_metal.api_client import ApiClient
from equinix_metal.configuration import Configuration
from equinix_metal.exceptions import OpenApiException
from equinix_metal.exceptions import ApiTypeError
from equinix_metal.exceptions import ApiValueError
from equinix_metal.exceptions import ApiKeyError
from equinix_metal.exceptions import ApiAttributeError
from equinix_metal.exceptions import ApiException

# import models into sdk package
from equinix_metal.models.aws_fabric_provider import AWSFabricProvider
from equinix_metal.models.activate_hardware_reservation_request import ActivateHardwareReservationRequest
from equinix_metal.models.address import Address
from equinix_metal.models.attribute import Attribute
from equinix_metal.models.attribute_data import AttributeData
from equinix_metal.models.auth_token import AuthToken
from equinix_metal.models.auth_token_input import AuthTokenInput
from equinix_metal.models.auth_token_list import AuthTokenList
from equinix_metal.models.auth_token_project import AuthTokenProject
from equinix_metal.models.auth_token_user import AuthTokenUser
from equinix_metal.models.bgp_session_input import BGPSessionInput
from equinix_metal.models.batch import Batch
from equinix_metal.models.batches_list import BatchesList
from equinix_metal.models.bgp_config import BgpConfig
from equinix_metal.models.bgp_config_request_input import BgpConfigRequestInput
from equinix_metal.models.bgp_dynamic_neighbor import BgpDynamicNeighbor
from equinix_metal.models.bgp_dynamic_neighbor_create_input import BgpDynamicNeighborCreateInput
from equinix_metal.models.bgp_dynamic_neighbor_list import BgpDynamicNeighborList
from equinix_metal.models.bgp_neighbor_data import BgpNeighborData
from equinix_metal.models.bgp_route import BgpRoute
from equinix_metal.models.bgp_session import BgpSession
from equinix_metal.models.bgp_session_list import BgpSessionList
from equinix_metal.models.bgp_session_neighbors import BgpSessionNeighbors
from equinix_metal.models.bond_port_data import BondPortData
from equinix_metal.models.capacity_check_per_facility_info import CapacityCheckPerFacilityInfo
from equinix_metal.models.capacity_check_per_facility_list import CapacityCheckPerFacilityList
from equinix_metal.models.capacity_check_per_metro_info import CapacityCheckPerMetroInfo
from equinix_metal.models.capacity_check_per_metro_list import CapacityCheckPerMetroList
from equinix_metal.models.capacity_input import CapacityInput
from equinix_metal.models.capacity_level_per_baremetal import CapacityLevelPerBaremetal
from equinix_metal.models.capacity_list import CapacityList
from equinix_metal.models.component import Component
from equinix_metal.models.coordinates import Coordinates
from equinix_metal.models.create_device_request import CreateDeviceRequest
from equinix_metal.models.create_email_input import CreateEmailInput
from equinix_metal.models.create_metal_gateway_request import CreateMetalGatewayRequest
from equinix_metal.models.create_organization_interconnection_request import CreateOrganizationInterconnectionRequest
from equinix_metal.models.create_self_service_reservation_request import CreateSelfServiceReservationRequest
from equinix_metal.models.create_self_service_reservation_request_period import CreateSelfServiceReservationRequestPeriod
from equinix_metal.models.dedicated_port_create_input import DedicatedPortCreateInput
from equinix_metal.models.device import Device
from equinix_metal.models.device_action_input import DeviceActionInput
from equinix_metal.models.device_actions_inner import DeviceActionsInner
from equinix_metal.models.device_create_in_facility_input import DeviceCreateInFacilityInput
from equinix_metal.models.device_create_in_metro_input import DeviceCreateInMetroInput
from equinix_metal.models.device_create_input import DeviceCreateInput
from equinix_metal.models.device_created_by import DeviceCreatedBy
from equinix_metal.models.device_health_rollup import DeviceHealthRollup
from equinix_metal.models.device_list import DeviceList
from equinix_metal.models.device_metro import DeviceMetro
from equinix_metal.models.device_project_lite import DeviceProjectLite
from equinix_metal.models.device_update_input import DeviceUpdateInput
from equinix_metal.models.device_usage import DeviceUsage
from equinix_metal.models.device_usage_list import DeviceUsageList
from equinix_metal.models.disk import Disk
from equinix_metal.models.email import Email
from equinix_metal.models.email_input import EmailInput
from equinix_metal.models.entitlement import Entitlement
from equinix_metal.models.error import Error
from equinix_metal.models.event import Event
from equinix_metal.models.event_list import EventList
from equinix_metal.models.fabric_service_token import FabricServiceToken
from equinix_metal.models.facility import Facility
from equinix_metal.models.facility_input import FacilityInput
from equinix_metal.models.facility_input_facility import FacilityInputFacility
from equinix_metal.models.facility_list import FacilityList
from equinix_metal.models.filesystem import Filesystem
from equinix_metal.models.find_ip_address_by_id200_response import FindIPAddressById200Response
from equinix_metal.models.find_metal_gateway_by_id200_response import FindMetalGatewayById200Response
from equinix_metal.models.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter
from equinix_metal.models.firmware_set import FirmwareSet
from equinix_metal.models.firmware_set_list_response import FirmwareSetListResponse
from equinix_metal.models.firmware_set_response import FirmwareSetResponse
from equinix_metal.models.global_bgp_range import GlobalBgpRange
from equinix_metal.models.global_bgp_range_list import GlobalBgpRangeList
from equinix_metal.models.hardware_reservation import HardwareReservation
from equinix_metal.models.hardware_reservation_list import HardwareReservationList
from equinix_metal.models.href import Href
from equinix_metal.models.ip_address import IPAddress
from equinix_metal.models.ip_assignment import IPAssignment
from equinix_metal.models.ip_assignment_input import IPAssignmentInput
from equinix_metal.models.ip_assignment_list import IPAssignmentList
from equinix_metal.models.ip_assignment_metro import IPAssignmentMetro
from equinix_metal.models.ip_assignment_update_input import IPAssignmentUpdateInput
from equinix_metal.models.ip_availabilities_list import IPAvailabilitiesList
from equinix_metal.models.ip_reservation import IPReservation
from equinix_metal.models.ip_reservation_facility import IPReservationFacility
from equinix_metal.models.ip_reservation_list import IPReservationList
from equinix_metal.models.ip_reservation_list_ip_addresses_inner import IPReservationListIpAddressesInner
from equinix_metal.models.ip_reservation_metro import IPReservationMetro
from equinix_metal.models.ip_reservation_request_input import IPReservationRequestInput
from equinix_metal.models.instances_batch_create_input import InstancesBatchCreateInput
from equinix_metal.models.instances_batch_create_input_batches_inner import InstancesBatchCreateInputBatchesInner
from equinix_metal.models.interconnection import Interconnection
from equinix_metal.models.interconnection_fabric_provider import InterconnectionFabricProvider
from equinix_metal.models.interconnection_list import InterconnectionList
from equinix_metal.models.interconnection_metro_list import InterconnectionMetroList
from equinix_metal.models.interconnection_metro_list_metros_inner import InterconnectionMetroListMetrosInner
from equinix_metal.models.interconnection_metro_list_metros_inner_all_of_providers_inner import InterconnectionMetroListMetrosInnerAllOfProvidersInner
from equinix_metal.models.interconnection_port import InterconnectionPort
from equinix_metal.models.interconnection_port_list import InterconnectionPortList
from equinix_metal.models.interconnection_pricing_list import InterconnectionPricingList
from equinix_metal.models.interconnection_pricing_list_provider_pricing_inner import InterconnectionPricingListProviderPricingInner
from equinix_metal.models.interconnection_pricing_list_provider_pricing_inner_tiers_inner import InterconnectionPricingListProviderPricingInnerTiersInner
from equinix_metal.models.interconnection_update_input import InterconnectionUpdateInput
from equinix_metal.models.invitation import Invitation
from equinix_metal.models.invitation_input import InvitationInput
from equinix_metal.models.invitation_list import InvitationList
from equinix_metal.models.invoice import Invoice
from equinix_metal.models.invoice_list import InvoiceList
from equinix_metal.models.license import License
from equinix_metal.models.license_create_input import LicenseCreateInput
from equinix_metal.models.license_list import LicenseList
from equinix_metal.models.license_update_input import LicenseUpdateInput
from equinix_metal.models.line_item import LineItem
from equinix_metal.models.line_item_adjustment import LineItemAdjustment
from equinix_metal.models.membership import Membership
from equinix_metal.models.membership_input import MembershipInput
from equinix_metal.models.membership_list import MembershipList
from equinix_metal.models.meta import Meta
from equinix_metal.models.metadata import Metadata
from equinix_metal.models.metadata_network import MetadataNetwork
from equinix_metal.models.metadata_network_network import MetadataNetworkNetwork
from equinix_metal.models.metadata_network_network_bonding import MetadataNetworkNetworkBonding
from equinix_metal.models.metal_gateway import MetalGateway
from equinix_metal.models.metal_gateway_create_input import MetalGatewayCreateInput
from equinix_metal.models.metal_gateway_elastic_ip_create_input import MetalGatewayElasticIpCreateInput
from equinix_metal.models.metal_gateway_list import MetalGatewayList
from equinix_metal.models.metal_gateway_list_metal_gateways_inner import MetalGatewayListMetalGatewaysInner
from equinix_metal.models.metal_gateway_lite import MetalGatewayLite
from equinix_metal.models.metro import Metro
from equinix_metal.models.metro_input import MetroInput
from equinix_metal.models.metro_list import MetroList
from equinix_metal.models.mount import Mount
from equinix_metal.models.move_hardware_reservation_request import MoveHardwareReservationRequest
from equinix_metal.models.new_password import NewPassword
from equinix_metal.models.operating_system import OperatingSystem
from equinix_metal.models.operating_system_list import OperatingSystemList
from equinix_metal.models.organization import Organization
from equinix_metal.models.organization_input import OrganizationInput
from equinix_metal.models.organization_list import OrganizationList
from equinix_metal.models.parent_block import ParentBlock
from equinix_metal.models.partition import Partition
from equinix_metal.models.payment_method import PaymentMethod
from equinix_metal.models.payment_method_billing_address import PaymentMethodBillingAddress
from equinix_metal.models.payment_method_create_input import PaymentMethodCreateInput
from equinix_metal.models.payment_method_list import PaymentMethodList
from equinix_metal.models.payment_method_update_input import PaymentMethodUpdateInput
from equinix_metal.models.plan import Plan
from equinix_metal.models.plan_available_in_inner import PlanAvailableInInner
from equinix_metal.models.plan_available_in_inner_price import PlanAvailableInInnerPrice
from equinix_metal.models.plan_available_in_metros_inner import PlanAvailableInMetrosInner
from equinix_metal.models.plan_id_name import PlanIdName
from equinix_metal.models.plan_list import PlanList
from equinix_metal.models.plan_specs import PlanSpecs
from equinix_metal.models.plan_specs_cpus_inner import PlanSpecsCpusInner
from equinix_metal.models.plan_specs_drives_inner import PlanSpecsDrivesInner
from equinix_metal.models.plan_specs_features import PlanSpecsFeatures
from equinix_metal.models.plan_specs_memory import PlanSpecsMemory
from equinix_metal.models.plan_specs_nics_inner import PlanSpecsNicsInner
from equinix_metal.models.port import Port
from equinix_metal.models.port_assign_input import PortAssignInput
from equinix_metal.models.port_convert_layer3_input import PortConvertLayer3Input
from equinix_metal.models.port_convert_layer3_input_request_ips_inner import PortConvertLayer3InputRequestIpsInner
from equinix_metal.models.port_data import PortData
from equinix_metal.models.port_vlan_assignment import PortVlanAssignment
from equinix_metal.models.port_vlan_assignment_batch import PortVlanAssignmentBatch
from equinix_metal.models.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput
from equinix_metal.models.port_vlan_assignment_batch_create_input_vlan_assignments_inner import PortVlanAssignmentBatchCreateInputVlanAssignmentsInner
from equinix_metal.models.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList
from equinix_metal.models.port_vlan_assignment_batch_vlan_assignments_inner import PortVlanAssignmentBatchVlanAssignmentsInner
from equinix_metal.models.port_vlan_assignment_list import PortVlanAssignmentList
from equinix_metal.models.project import Project
from equinix_metal.models.project_create_from_root_input import ProjectCreateFromRootInput
from equinix_metal.models.project_create_input import ProjectCreateInput
from equinix_metal.models.project_id_name import ProjectIdName
from equinix_metal.models.project_list import ProjectList
from equinix_metal.models.project_update_input import ProjectUpdateInput
from equinix_metal.models.project_usage import ProjectUsage
from equinix_metal.models.project_usage_list import ProjectUsageList
from equinix_metal.models.raid import Raid
from equinix_metal.models.recovery_code_list import RecoveryCodeList
from equinix_metal.models.request_ip_reservation201_response import RequestIPReservation201Response
from equinix_metal.models.request_ip_reservation_request import RequestIPReservationRequest
from equinix_metal.models.ssh_key import SSHKey
from equinix_metal.models.ssh_key_create_input import SSHKeyCreateInput
from equinix_metal.models.ssh_key_input import SSHKeyInput
from equinix_metal.models.ssh_key_list import SSHKeyList
from equinix_metal.models.self_service_reservation_item_request import SelfServiceReservationItemRequest
from equinix_metal.models.self_service_reservation_item_response import SelfServiceReservationItemResponse
from equinix_metal.models.self_service_reservation_list import SelfServiceReservationList
from equinix_metal.models.self_service_reservation_response import SelfServiceReservationResponse
from equinix_metal.models.server_info import ServerInfo
from equinix_metal.models.shared_port_vc_vlan_create_input import SharedPortVCVlanCreateInput
from equinix_metal.models.spot_market_prices_list import SpotMarketPricesList
from equinix_metal.models.spot_market_prices_per_metro_list import SpotMarketPricesPerMetroList
from equinix_metal.models.spot_market_prices_per_metro_report import SpotMarketPricesPerMetroReport
from equinix_metal.models.spot_market_request import SpotMarketRequest
from equinix_metal.models.spot_market_request_create_input import SpotMarketRequestCreateInput
from equinix_metal.models.spot_market_request_create_input_instance_parameters import SpotMarketRequestCreateInputInstanceParameters
from equinix_metal.models.spot_market_request_list import SpotMarketRequestList
from equinix_metal.models.spot_market_request_metro import SpotMarketRequestMetro
from equinix_metal.models.spot_prices_datapoints import SpotPricesDatapoints
from equinix_metal.models.spot_prices_history_report import SpotPricesHistoryReport
from equinix_metal.models.spot_prices_per_baremetal import SpotPricesPerBaremetal
from equinix_metal.models.spot_prices_per_facility import SpotPricesPerFacility
from equinix_metal.models.spot_prices_per_new_facility import SpotPricesPerNewFacility
from equinix_metal.models.spot_prices_report import SpotPricesReport
from equinix_metal.models.storage import Storage
from equinix_metal.models.support_request_input import SupportRequestInput
from equinix_metal.models.transfer_request import TransferRequest
from equinix_metal.models.transfer_request_input import TransferRequestInput
from equinix_metal.models.transfer_request_list import TransferRequestList
from equinix_metal.models.update_email_input import UpdateEmailInput
from equinix_metal.models.user import User
from equinix_metal.models.user_create_input import UserCreateInput
from equinix_metal.models.user_limited import UserLimited
from equinix_metal.models.user_list import UserList
from equinix_metal.models.user_lite import UserLite
from equinix_metal.models.user_update_input import UserUpdateInput
from equinix_metal.models.userdata import Userdata
from equinix_metal.models.verify_email import VerifyEmail
from equinix_metal.models.virtual_circuit import VirtualCircuit
from equinix_metal.models.virtual_circuit_create_input import VirtualCircuitCreateInput
from equinix_metal.models.virtual_circuit_list import VirtualCircuitList
from equinix_metal.models.virtual_circuit_update_input import VirtualCircuitUpdateInput
from equinix_metal.models.virtual_network import VirtualNetwork
from equinix_metal.models.virtual_network_create_input import VirtualNetworkCreateInput
from equinix_metal.models.virtual_network_list import VirtualNetworkList
from equinix_metal.models.virtual_network_update_input import VirtualNetworkUpdateInput
from equinix_metal.models.vlan_csp_connection_create_input import VlanCSPConnectionCreateInput
from equinix_metal.models.vlan_csp_connection_create_input_fabric_provider import VlanCSPConnectionCreateInputFabricProvider
from equinix_metal.models.vlan_fabric_vc_create_input import VlanFabricVcCreateInput
from equinix_metal.models.vlan_virtual_circuit import VlanVirtualCircuit
from equinix_metal.models.vlan_virtual_circuit_create_input import VlanVirtualCircuitCreateInput
from equinix_metal.models.vlan_virtual_circuit_update_input import VlanVirtualCircuitUpdateInput
from equinix_metal.models.vrf import Vrf
from equinix_metal.models.vrf_bgp_neighbors import VrfBGPNeighbors
from equinix_metal.models.vrf_bgp_neighbors_list import VrfBGPNeighborsList
from equinix_metal.models.vrf_create_input import VrfCreateInput
from equinix_metal.models.vrf_fabric_vc_create_input import VrfFabricVcCreateInput
from equinix_metal.models.vrf_ip_reservation import VrfIpReservation
from equinix_metal.models.vrf_ip_reservation_create_input import VrfIpReservationCreateInput
from equinix_metal.models.vrf_ip_reservation_list import VrfIpReservationList
from equinix_metal.models.vrf_learned_routes import VrfLearnedRoutes
from equinix_metal.models.vrf_learned_routes_list import VrfLearnedRoutesList
from equinix_metal.models.vrf_list import VrfList
from equinix_metal.models.vrf_metal_gateway import VrfMetalGateway
from equinix_metal.models.vrf_metal_gateway_create_input import VrfMetalGatewayCreateInput
from equinix_metal.models.vrf_route import VrfRoute
from equinix_metal.models.vrf_route_create_input import VrfRouteCreateInput
from equinix_metal.models.vrf_route_list import VrfRouteList
from equinix_metal.models.vrf_route_update_input import VrfRouteUpdateInput
from equinix_metal.models.vrf_update_input import VrfUpdateInput
from equinix_metal.models.vrf_virtual_circuit import VrfVirtualCircuit
from equinix_metal.models.vrf_virtual_circuit_create_input import VrfVirtualCircuitCreateInput
from equinix_metal.models.vrf_virtual_circuit_update_input import VrfVirtualCircuitUpdateInput