# RemoveOperation

Remove sub-resource from an existing model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**OpEnum**](OpEnum.md) |  | 
**path** | **str** | A JSON Pointer path. | 

## Example

```python
from equinix.services.fabricv4.models.remove_operation import RemoveOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveOperation from a JSON string
remove_operation_instance = RemoveOperation.from_json(json)
# print the JSON string representation of the object
print(RemoveOperation.to_json())

# convert the object into a dict
remove_operation_dict = remove_operation_instance.to_dict()
# create an instance of RemoveOperation from a dict
remove_operation_from_dict = RemoveOperation.from_dict(remove_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


