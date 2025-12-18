# CompanyProfileUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_profile** | [**CompanyProfileResponse**](CompanyProfileResponse.md) |  | [optional] 
**change** | [**CompanyProfileChange**](CompanyProfileChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_update_response import CompanyProfileUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileUpdateResponse from a JSON string
company_profile_update_response_instance = CompanyProfileUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileUpdateResponse.to_json())

# convert the object into a dict
company_profile_update_response_dict = company_profile_update_response_instance.to_dict()
# create an instance of CompanyProfileUpdateResponse from a dict
company_profile_update_response_from_dict = CompanyProfileUpdateResponse.from_dict(company_profile_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


