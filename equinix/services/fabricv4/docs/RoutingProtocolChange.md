# RoutingProtocolChange

Current state of latest Routing Protocol change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RoutingProtocolChangeType**](RoutingProtocolChangeType.md) |  | 
**href** | **str** | Routing Protocol Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_change import RoutingProtocolChange

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolChange from a JSON string
routing_protocol_change_instance = RoutingProtocolChange.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolChange.to_json())

# convert the object into a dict
routing_protocol_change_dict = routing_protocol_change_instance.to_dict()
# create an instance of RoutingProtocolChange from a dict
routing_protocol_change_from_dict = RoutingProtocolChange.from_dict(routing_protocol_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


