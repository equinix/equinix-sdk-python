# CompanyProfileResponseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_org_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_response_account import CompanyProfileResponseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileResponseAccount from a JSON string
company_profile_response_account_instance = CompanyProfileResponseAccount.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileResponseAccount.to_json())

# convert the object into a dict
company_profile_response_account_dict = company_profile_response_account_instance.to_dict()
# create an instance of CompanyProfileResponseAccount from a dict
company_profile_response_account_from_dict = CompanyProfileResponseAccount.from_dict(company_profile_response_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


