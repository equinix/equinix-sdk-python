# SSHKeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ssh_keys** | [**List[SSHKey]**](SSHKey.md) |  | [optional] 

## Example

```python
from equinix_metal.models.ssh_key_list import SSHKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of SSHKeyList from a JSON string
ssh_key_list_instance = SSHKeyList.from_json(json)
# print the JSON string representation of the object
print(SSHKeyList.to_json())

# convert the object into a dict
ssh_key_list_dict = ssh_key_list_instance.to_dict()
# create an instance of SSHKeyList from a dict
ssh_key_list_form_dict = ssh_key_list.from_dict(ssh_key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


