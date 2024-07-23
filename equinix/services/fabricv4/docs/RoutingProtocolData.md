# RoutingProtocolData


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
**bfd** | [**RoutingProtocolBFD**](RoutingProtocolBFD.md) |  | [optional] 
**href** | **str** | Routing Protocol URI | [optional] 
**uuid** | **str** | Routing protocol identifier | [optional] 
**state** | [**RoutingProtocolBGPDataState**](RoutingProtocolBGPDataState.md) |  | [optional] 
**operation** | [**RoutingProtocolOperation**](RoutingProtocolOperation.md) |  | [optional] 
**change** | [**RoutingProtocolChange**](RoutingProtocolChange.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 
**direct_ipv4** | [**DirectConnectionIpv4**](DirectConnectionIpv4.md) |  | [optional] 
**direct_ipv6** | [**DirectConnectionIpv6**](DirectConnectionIpv6.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_data import RoutingProtocolData

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolData from a JSON string
routing_protocol_data_instance = RoutingProtocolData.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolData.to_json())

# convert the object into a dict
routing_protocol_data_dict = routing_protocol_data_instance.to_dict()
# create an instance of RoutingProtocolData from a dict
routing_protocol_data_form_dict = routing_protocol_data.from_dict(routing_protocol_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


