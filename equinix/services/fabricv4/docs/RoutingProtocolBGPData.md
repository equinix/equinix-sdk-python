# RoutingProtocolBGPData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoutingProtocolBGPTypeType**](RoutingProtocolBGPTypeType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**bgp_ipv4** | [**BGPConnectionIpv4**](BGPConnectionIpv4.md) |  | [optional] 
**bgp_ipv6** | [**BGPConnectionIpv6**](BGPConnectionIpv6.md) |  | [optional] 
**customer_asn** | **int** | Customer asn | [optional] 
**equinix_asn** | **int** | Equinix asn | [optional] 
**bgp_auth_key** | **str** | BGP authorization key | [optional] 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**bfd** | [**RoutingProtocolBFD**](RoutingProtocolBFD.md) |  | [optional] 
**href** | **str** | Routing Protocol URI | [optional] 
**uuid** | **str** | Routing protocol identifier | [optional] 
**state** | [**RoutingProtocolBGPDataState**](RoutingProtocolBGPDataState.md) |  | [optional] 
**operation** | [**RoutingProtocolOperation**](RoutingProtocolOperation.md) |  | [optional] 
**change** | [**RoutingProtocolChange**](RoutingProtocolChange.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_bgp_data import RoutingProtocolBGPData

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolBGPData from a JSON string
routing_protocol_bgp_data_instance = RoutingProtocolBGPData.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolBGPData.to_json())

# convert the object into a dict
routing_protocol_bgp_data_dict = routing_protocol_bgp_data_instance.to_dict()
# create an instance of RoutingProtocolBGPData from a dict
routing_protocol_bgp_data_form_dict = routing_protocol_bgp_data.from_dict(routing_protocol_bgp_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


