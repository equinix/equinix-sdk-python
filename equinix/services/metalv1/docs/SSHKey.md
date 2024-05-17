# SSHKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**entity** | [**Href**](Href.md) |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.ssh_key import SSHKey

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKey from a JSON string
ssh_key_instance = SSHKey.from_json(json)
# print the JSON string representation of the object
print(SSHKey.to_json())

# convert the object into a dict
ssh_key_dict = ssh_key_instance.to_dict()
# create an instance of SSHKey from a dict
ssh_key_form_dict = ssh_key.from_dict(ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


