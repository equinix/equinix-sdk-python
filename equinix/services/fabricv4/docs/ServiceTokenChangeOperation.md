# ServiceTokenChangeOperation

Service Token change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.service_token_change_operation import ServiceTokenChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenChangeOperation from a JSON string
service_token_change_operation_instance = ServiceTokenChangeOperation.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenChangeOperation.to_json())

# convert the object into a dict
service_token_change_operation_dict = service_token_change_operation_instance.to_dict()
# create an instance of ServiceTokenChangeOperation from a dict
service_token_change_operation_form_dict = service_token_change_operation.from_dict(service_token_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


