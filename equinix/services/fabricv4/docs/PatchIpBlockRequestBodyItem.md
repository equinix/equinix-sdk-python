# PatchIpBlockRequestBodyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**PatchIpBlockRequestBodyItemOp**](PatchIpBlockRequestBodyItemOp.md) |  | 
**path** | **str** | path | 
**value** | [**PatchIpBlockRequestBodyItemValue**](PatchIpBlockRequestBodyItemValue.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.patch_ip_block_request_body_item import PatchIpBlockRequestBodyItem

# TODO update the JSON string below
json = "{}"
# create an instance of PatchIpBlockRequestBodyItem from a JSON string
patch_ip_block_request_body_item_instance = PatchIpBlockRequestBodyItem.from_json(json)
# print the JSON string representation of the object
print(PatchIpBlockRequestBodyItem.to_json())

# convert the object into a dict
patch_ip_block_request_body_item_dict = patch_ip_block_request_body_item_instance.to_dict()
# create an instance of PatchIpBlockRequestBodyItem from a dict
patch_ip_block_request_body_item_from_dict = PatchIpBlockRequestBodyItem.from_dict(patch_ip_block_request_body_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


