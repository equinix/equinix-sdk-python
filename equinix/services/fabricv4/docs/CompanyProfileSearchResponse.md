# CompanyProfileSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**data** | [**List[CompanyProfileResponse]**](CompanyProfileResponse.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.company_profile_search_response import CompanyProfileSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileSearchResponse from a JSON string
company_profile_search_response_instance = CompanyProfileSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileSearchResponse.to_json())

# convert the object into a dict
company_profile_search_response_dict = company_profile_search_response_instance.to_dict()
# create an instance of CompanyProfileSearchResponse from a dict
company_profile_search_response_from_dict = CompanyProfileSearchResponse.from_dict(company_profile_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


