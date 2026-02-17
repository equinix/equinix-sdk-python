# CompanyProfileSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CompanyProfileSearchFilter**](CompanyProfileSearchFilter.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**Sort**](Sort.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_search_request import CompanyProfileSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileSearchRequest from a JSON string
company_profile_search_request_instance = CompanyProfileSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileSearchRequest.to_json())

# convert the object into a dict
company_profile_search_request_dict = company_profile_search_request_instance.to_dict()
# create an instance of CompanyProfileSearchRequest from a dict
company_profile_search_request_from_dict = CompanyProfileSearchRequest.from_dict(company_profile_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


