# SSHKeyCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**instances_ids** | **List[str]** | List of instance UUIDs to associate SSH key with, when empty array is sent all instances belonging       to entity will be included | [optional] 
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.ssh_key_create_input import SSHKeyCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKeyCreateInput from a JSON string
ssh_key_create_input_instance = SSHKeyCreateInput.from_json(json)
# print the JSON string representation of the object
print(SSHKeyCreateInput.to_json())

# convert the object into a dict
ssh_key_create_input_dict = ssh_key_create_input_instance.to_dict()
# create an instance of SSHKeyCreateInput from a dict
ssh_key_create_input_form_dict = ssh_key_create_input.from_dict(ssh_key_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


