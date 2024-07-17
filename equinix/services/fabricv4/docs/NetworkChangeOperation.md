# NetworkChangeOperation

Network change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.network_change_operation import NetworkChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkChangeOperation from a JSON string
network_change_operation_instance = NetworkChangeOperation.from_json(json)
# print the JSON string representation of the object
print(NetworkChangeOperation.to_json())

# convert the object into a dict
network_change_operation_dict = network_change_operation_instance.to_dict()
# create an instance of NetworkChangeOperation from a dict
network_change_operation_form_dict = network_change_operation.from_dict(network_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


