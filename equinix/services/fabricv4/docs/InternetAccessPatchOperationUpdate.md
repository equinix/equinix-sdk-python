# InternetAccessPatchOperationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**InternetAccessPatchOperationUpdateAllowedOp**](InternetAccessPatchOperationUpdateAllowedOp.md) |  | 
**path** | **str** | Allowed patch paths for Internet Access update. | 
**value** | **object** | New value for updated parameter. Required for add and replace. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_patch_operation_update import InternetAccessPatchOperationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPatchOperationUpdate from a JSON string
internet_access_patch_operation_update_instance = InternetAccessPatchOperationUpdate.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPatchOperationUpdate.to_json())

# convert the object into a dict
internet_access_patch_operation_update_dict = internet_access_patch_operation_update_instance.to_dict()
# create an instance of InternetAccessPatchOperationUpdate from a dict
internet_access_patch_operation_update_from_dict = InternetAccessPatchOperationUpdate.from_dict(internet_access_patch_operation_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


