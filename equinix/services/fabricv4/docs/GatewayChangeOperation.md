# GatewayChangeOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.gateway_change_operation import GatewayChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayChangeOperation from a JSON string
gateway_change_operation_instance = GatewayChangeOperation.from_json(json)
# print the JSON string representation of the object
print(GatewayChangeOperation.to_json())

# convert the object into a dict
gateway_change_operation_dict = gateway_change_operation_instance.to_dict()
# create an instance of GatewayChangeOperation from a dict
gateway_change_operation_from_dict = GatewayChangeOperation.from_dict(gateway_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


