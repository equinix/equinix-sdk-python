# RoutingProtocolDirectData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoutingProtocolDirectTypeType**](RoutingProtocolDirectTypeType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**direct_ipv4** | [**DirectConnectionIpv4**](DirectConnectionIpv4.md) |  | [optional] 
**direct_ipv6** | [**DirectConnectionIpv6**](DirectConnectionIpv6.md) |  | [optional] 
**href** | **str** | Routing Protocol URI | [optional] 
**uuid** | **str** | Routing protocol identifier | [optional] 
**state** | [**RoutingProtocolBGPDataState**](RoutingProtocolBGPDataState.md) |  | [optional] 
**operation** | [**RoutingProtocolOperation**](RoutingProtocolOperation.md) |  | [optional] 
**change** | [**RoutingProtocolChange**](RoutingProtocolChange.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_direct_data import RoutingProtocolDirectData

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolDirectData from a JSON string
routing_protocol_direct_data_instance = RoutingProtocolDirectData.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolDirectData.to_json())

# convert the object into a dict
routing_protocol_direct_data_dict = routing_protocol_direct_data_instance.to_dict()
# create an instance of RoutingProtocolDirectData from a dict
routing_protocol_direct_data_form_dict = routing_protocol_direct_data.from_dict(routing_protocol_direct_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


