from __future__ import annotations

from equinix.services import fabricv4

from . import token_generator
from .users import UserName


class Apis:
    def __init__(self, api_client: fabricv4.ApiClient) -> None:
        self.api_client = api_client
        self.cloud_routers = fabricv4.CloudRoutersApi(api_client)
        self.connections = fabricv4.ConnectionsApi(api_client)
        self.health = fabricv4.HealthApi(api_client)
        self.metros = fabricv4.MetrosApi(api_client)
        self.networks = fabricv4.NetworksApi(api_client)
        self.ports = fabricv4.PortsApi(api_client)
        self.precision_time = fabricv4.PrecisionTimeApi(api_client)
        self.prices = fabricv4.PricesApi(api_client)
        self.route_filters = fabricv4.RouteFiltersApi(api_client)
        self.route_filter_rules = fabricv4.RouteFilterRulesApi(api_client)
        self.routing_protocols = fabricv4.RoutingProtocolsApi(api_client)
        self.service_profiles = fabricv4.ServiceProfilesApi(api_client)
        self.service_tokens = fabricv4.ServiceTokensApi(api_client)
        self.statistics = fabricv4.StatisticsApi(api_client)
        self.internet_access_services = fabricv4.InternetAccessServicesApi(api_client)
        self.ip_blocks = fabricv4.IPBlocksApi(api_client)
        self.loa = fabricv4.LoasApi(api_client)
        self.ix = fabricv4.InternetExchangeServicesApi(api_client)


def for_user(user_name: UserName) -> Apis:
    return Apis(token_generator.get_api_client(user_name))
