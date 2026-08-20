# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Account identifier | [optional] 
**account_number** | **int** | Account number | [optional] 
**account_name** | **str** | Account name | [optional] 
**ucm_id** | **str** | Account ucm id | [optional] 
**global_cust_id** | **str** | Global customer organization id | [optional] 
**org_id** | **int** | Customer organization id | [optional] 
**organization_name** | **str** | Customer organization name | [optional] 
**sub_customes** | [**List[Account]**](Account.md) | All sub customer accounts | [optional] 
**country_code** | **str** | Account country code | [optional] 
**operational_unit** | **str** | Account operational unit | [optional] 
**operational_unit_metros** | **List[str]** | Account operational unit metros | [optional] 
**signature_required** | **bool** | Is signature required | [optional] 
**po_bearing** | **bool** | Purchase order bearing | [optional] 
**default** | **bool** | Default account or not | [optional] 

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


