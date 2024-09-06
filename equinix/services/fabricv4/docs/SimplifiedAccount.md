# SimplifiedAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** | Account number | [optional] 
**account_name** | **str** | Account name | [optional] 
**org_id** | **int** | Customer organization identifier | [optional] 
**organization_name** | **str** | Customer organization name | [optional] 
**global_org_id** | **str** | Global organization identifier | [optional] 
**global_organization_name** | **str** | Global organization name | [optional] 
**ucm_id** | **str** | Account ucmId | [optional] 
**global_cust_id** | **str** | Account name | [optional] 
**reseller_account_number** | **int** | Reseller account number | [optional] 
**reseller_account_name** | **str** | Reseller account name | [optional] 
**reseller_ucm_id** | **str** | Reseller account ucmId | [optional] 
**reseller_org_id** | **int** | Reseller customer organization identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_account import SimplifiedAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedAccount from a JSON string
simplified_account_instance = SimplifiedAccount.from_json(json)
# print the JSON string representation of the object
print(SimplifiedAccount.to_json())

# convert the object into a dict
simplified_account_dict = simplified_account_instance.to_dict()
# create an instance of SimplifiedAccount from a dict
simplified_account_from_dict = SimplifiedAccount.from_dict(simplified_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


