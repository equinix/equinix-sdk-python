# Account

Account model, includes account number and flag to indicate if this account is reseller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** |  | 
**is_reseller_account** | **bool** |  | [optional] 
**org_id** | **str** |  | [optional] 
**global_org_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


