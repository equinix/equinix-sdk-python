# AddOperation

Add Sub-Resource to the existing model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**OpEnum**](OpEnum.md) |  | 
**path** | **str** | A JSON Pointer path. | 
**value** | **object** | value to add | 

## Example

```python
from equinix.services.fabricv4.models.add_operation import AddOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AddOperation from a JSON string
add_operation_instance = AddOperation.from_json(json)
# print the JSON string representation of the object
print(AddOperation.to_json())

# convert the object into a dict
add_operation_dict = add_operation_instance.to_dict()
# create an instance of AddOperation from a dict
add_operation_from_dict = AddOperation.from_dict(add_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


