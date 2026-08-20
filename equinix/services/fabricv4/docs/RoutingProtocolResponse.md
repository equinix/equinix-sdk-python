# RoutingProtocolResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_asn** | **str** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**vlan** | **int** | VLAN ID | [optional] 
**route_server_asn** | **int** | Equinix Route Server ASN | [optional] 
**bgp_ipv4** | [**ExchangeServiceResponseBgp**](ExchangeServiceResponseBgp.md) |  | [optional] 
**bgp_ipv6** | [**ExchangeServiceResponseBgp**](ExchangeServiceResponseBgp.md) |  | [optional] 
**route_collector** | [**RouteCollector**](RouteCollector.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_response import RoutingProtocolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolResponse from a JSON string
routing_protocol_response_instance = RoutingProtocolResponse.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolResponse.to_json())

# convert the object into a dict
routing_protocol_response_dict = routing_protocol_response_instance.to_dict()
# create an instance of RoutingProtocolResponse from a dict
routing_protocol_response_from_dict = RoutingProtocolResponse.from_dict(routing_protocol_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


