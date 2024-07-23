# RoutingProtocolChangeOperation

Routing Protocol change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**RoutingProtocolChangeOperationOp**](RoutingProtocolChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | [**RoutingProtocolBase**](RoutingProtocolBase.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_change_operation import RoutingProtocolChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolChangeOperation from a JSON string
routing_protocol_change_operation_instance = RoutingProtocolChangeOperation.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolChangeOperation.to_json())

# convert the object into a dict
routing_protocol_change_operation_dict = routing_protocol_change_operation_instance.to_dict()
# create an instance of RoutingProtocolChangeOperation from a dict
routing_protocol_change_operation_form_dict = routing_protocol_change_operation.from_dict(routing_protocol_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


