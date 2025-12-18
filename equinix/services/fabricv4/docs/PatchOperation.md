# PatchOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PatchOperationOp**](PatchOperationOp.md) |  | 
**path** | **str** | JSON Pointer path to the field to modify (e.g., /name, /description, /summary, /webUrl, /notifications) | 
**value** | **object** | The value to update the field to | 

## Example

```python
from equinix.services.fabricv4.models.patch_operation import PatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOperation from a JSON string
patch_operation_instance = PatchOperation.from_json(json)
# print the JSON string representation of the object
print(PatchOperation.to_json())

# convert the object into a dict
patch_operation_dict = patch_operation_instance.to_dict()
# create an instance of PatchOperation from a dict
patch_operation_from_dict = PatchOperation.from_dict(patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


