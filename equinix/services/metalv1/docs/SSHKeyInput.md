# SSHKeyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.ssh_key_input import SSHKeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKeyInput from a JSON string
ssh_key_input_instance = SSHKeyInput.from_json(json)
# print the JSON string representation of the object
print(SSHKeyInput.to_json())

# convert the object into a dict
ssh_key_input_dict = ssh_key_input_instance.to_dict()
# create an instance of SSHKeyInput from a dict
ssh_key_input_form_dict = ssh_key_input.from_dict(ssh_key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


