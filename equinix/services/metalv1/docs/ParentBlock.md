# ParentBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **int** |  | [optional] 
**href** | **str** |  | [optional] 
**netmask** | **str** |  | [optional] 
**network** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.parent_block import ParentBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ParentBlock from a JSON string
parent_block_instance = ParentBlock.from_json(json)
# print the JSON string representation of the object
print(ParentBlock.to_json())

# convert the object into a dict
parent_block_dict = parent_block_instance.to_dict()
# create an instance of ParentBlock from a dict
parent_block_form_dict = parent_block.from_dict(parent_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


