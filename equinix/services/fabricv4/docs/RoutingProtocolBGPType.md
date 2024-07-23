# RoutingProtocolBGPType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoutingProtocolBGPTypeType**](RoutingProtocolBGPTypeType.md) |  | 
**name** | **str** |  | [optional] 
**bgp_ipv4** | [**BGPConnectionIpv4**](BGPConnectionIpv4.md) |  | [optional] 
**bgp_ipv6** | [**BGPConnectionIpv6**](BGPConnectionIpv6.md) |  | [optional] 
**customer_asn** | **int** | Customer asn | [optional] 
**equinix_asn** | **int** | Equinix asn | [optional] 
**bgp_auth_key** | **str** | BGP authorization key | [optional] 
**bfd** | [**RoutingProtocolBFD**](RoutingProtocolBFD.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_bgp_type import RoutingProtocolBGPType

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolBGPType from a JSON string
routing_protocol_bgp_type_instance = RoutingProtocolBGPType.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolBGPType.to_json())

# convert the object into a dict
routing_protocol_bgp_type_dict = routing_protocol_bgp_type_instance.to_dict()
# create an instance of RoutingProtocolBGPType from a dict
routing_protocol_bgp_type_form_dict = routing_protocol_bgp_type.from_dict(routing_protocol_bgp_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


