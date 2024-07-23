# PrecisionTimeChangeOperation

Fabric Precision Timing change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | [**PrecisionTimeChangeOperationPath**](PrecisionTimeChangeOperationPath.md) |  | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.precision_time_change_operation import PrecisionTimeChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PrecisionTimeChangeOperation from a JSON string
precision_time_change_operation_instance = PrecisionTimeChangeOperation.from_json(json)
# print the JSON string representation of the object
print(PrecisionTimeChangeOperation.to_json())

# convert the object into a dict
precision_time_change_operation_dict = precision_time_change_operation_instance.to_dict()
# create an instance of PrecisionTimeChangeOperation from a dict
precision_time_change_operation_form_dict = precision_time_change_operation.from_dict(precision_time_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


