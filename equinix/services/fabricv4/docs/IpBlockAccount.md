# IpBlockAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | account number | 

## Example

```python
from equinix.services.fabricv4.models.ip_block_account import IpBlockAccount

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockAccount from a JSON string
ip_block_account_instance = IpBlockAccount.from_json(json)
# print the JSON string representation of the object
print(IpBlockAccount.to_json())

# convert the object into a dict
ip_block_account_dict = ip_block_account_instance.to_dict()
# create an instance of IpBlockAccount from a dict
ip_block_account_from_dict = IpBlockAccount.from_dict(ip_block_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


