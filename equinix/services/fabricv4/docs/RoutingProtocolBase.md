# RoutingProtocolBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Routing protocol type | [optional] 
**name** | **str** |  | [optional] 
**bgp_ipv4** | [**BGPConnectionIpv4**](BGPConnectionIpv4.md) |  | [optional] 
**bgp_ipv6** | [**BGPConnectionIpv6**](BGPConnectionIpv6.md) |  | [optional] 
**customer_asn** | **int** | Customer asn | [optional] 
**equinix_asn** | **int** | Equinix asn | [optional] 
**bgp_auth_key** | **str** | BGP authorization key | [optional] 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**bfd** | [**RoutingProtocolBFD**](RoutingProtocolBFD.md) |  | [optional] 
**direct_ipv4** | [**DirectConnectionIpv4**](DirectConnectionIpv4.md) |  | [optional] 
**direct_ipv6** | [**DirectConnectionIpv6**](DirectConnectionIpv6.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_base import RoutingProtocolBase

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolBase from a JSON string
routing_protocol_base_instance = RoutingProtocolBase.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolBase.to_json())

# convert the object into a dict
routing_protocol_base_dict = routing_protocol_base_instance.to_dict()
# create an instance of RoutingProtocolBase from a dict
routing_protocol_base_form_dict = routing_protocol_base.from_dict(routing_protocol_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


