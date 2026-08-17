# AppLinkChangeOperation

App Link change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PrecisionTimeChangeOperationOp**](PrecisionTimeChangeOperationOp.md) |  | 
**path** | [**AppLinkChangeOperationPath**](AppLinkChangeOperationPath.md) |  | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.app_link_change_operation import AppLinkChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkChangeOperation from a JSON string
app_link_change_operation_instance = AppLinkChangeOperation.from_json(json)
# print the JSON string representation of the object
print(AppLinkChangeOperation.to_json())

# convert the object into a dict
app_link_change_operation_dict = app_link_change_operation_instance.to_dict()
# create an instance of AppLinkChangeOperation from a dict
app_link_change_operation_from_dict = AppLinkChangeOperation.from_dict(app_link_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


