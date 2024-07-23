# RoutingProtocolDirectType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoutingProtocolDirectTypeType**](RoutingProtocolDirectTypeType.md) |  | 
**name** | **str** |  | [optional] 
**direct_ipv4** | [**DirectConnectionIpv4**](DirectConnectionIpv4.md) |  | [optional] 
**direct_ipv6** | [**DirectConnectionIpv6**](DirectConnectionIpv6.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_direct_type import RoutingProtocolDirectType

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolDirectType from a JSON string
routing_protocol_direct_type_instance = RoutingProtocolDirectType.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolDirectType.to_json())

# convert the object into a dict
routing_protocol_direct_type_dict = routing_protocol_direct_type_instance.to_dict()
# create an instance of RoutingProtocolDirectType from a dict
routing_protocol_direct_type_form_dict = routing_protocol_direct_type.from_dict(routing_protocol_direct_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


