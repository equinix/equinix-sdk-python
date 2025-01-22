# RoutingProtocolOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_operation import RoutingProtocolOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolOperation from a JSON string
routing_protocol_operation_instance = RoutingProtocolOperation.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolOperation.to_json())

# convert the object into a dict
routing_protocol_operation_dict = routing_protocol_operation_instance.to_dict()
# create an instance of RoutingProtocolOperation from a dict
routing_protocol_operation_from_dict = RoutingProtocolOperation.from_dict(routing_protocol_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


