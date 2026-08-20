# ServiceProfileUpdateOperation

Service Profile Access Points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**ReplaceOperationOp**](ReplaceOperationOp.md) |  | 
**path** | **str** | A JSON Pointer path. | 
**value** | **object** | value to replace with | 

## Example

```python
from equinix.services.fabricv4.models.service_profile_update_operation import ServiceProfileUpdateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileUpdateOperation from a JSON string
service_profile_update_operation_instance = ServiceProfileUpdateOperation.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileUpdateOperation.to_json())

# convert the object into a dict
service_profile_update_operation_dict = service_profile_update_operation_instance.to_dict()
# create an instance of ServiceProfileUpdateOperation from a dict
service_profile_update_operation_from_dict = ServiceProfileUpdateOperation.from_dict(service_profile_update_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


