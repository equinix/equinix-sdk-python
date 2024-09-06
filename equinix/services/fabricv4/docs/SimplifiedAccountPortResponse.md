# SimplifiedAccountPortResponse

Temporary SimplifiedAccount for PortResponse data mismatch of all strings in account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | Account number | [optional] 
**org_id** | **str** | Customer organization identifier | [optional] 
**reseller_account_number** | **str** | Reseller account number | [optional] 
**reseller_org_id** | **str** | Reseller customer organization identifier | [optional] 
**account_name** | **str** | Account name | [optional] 
**organization_name** | **str** | Customer organization name | [optional] 
**global_org_id** | **str** | Global organization identifier | [optional] 
**global_organization_name** | **str** | Global organization name | [optional] 
**ucm_id** | **str** | Account ucmId | [optional] 
**global_cust_id** | **str** | Account name | [optional] 
**reseller_account_name** | **str** | Reseller account name | [optional] 
**reseller_ucm_id** | **str** | Reseller account ucmId | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_account_port_response import SimplifiedAccountPortResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedAccountPortResponse from a JSON string
simplified_account_port_response_instance = SimplifiedAccountPortResponse.from_json(json)
# print the JSON string representation of the object
print(SimplifiedAccountPortResponse.to_json())

# convert the object into a dict
simplified_account_port_response_dict = simplified_account_port_response_instance.to_dict()
# create an instance of SimplifiedAccountPortResponse from a dict
simplified_account_port_response_from_dict = SimplifiedAccountPortResponse.from_dict(simplified_account_port_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


