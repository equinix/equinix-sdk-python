# AsnPatchOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**AsnPatchOperationOp**](AsnPatchOperationOp.md) |  | 
**path** | **str** | JSON Pointer to the field to update | 
**value** | **object** | New value for add or replace operations | 

## Example

```python
from equinix.services.fabricv4.models.asn_patch_operation import AsnPatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AsnPatchOperation from a JSON string
asn_patch_operation_instance = AsnPatchOperation.from_json(json)
# print the JSON string representation of the object
print(AsnPatchOperation.to_json())

# convert the object into a dict
asn_patch_operation_dict = asn_patch_operation_instance.to_dict()
# create an instance of AsnPatchOperation from a dict
asn_patch_operation_from_dict = AsnPatchOperation.from_dict(asn_patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


