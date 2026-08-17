# CompanyProfileSearchFilters

Filter criteria for company profile search. The `and` array combines conditions where all must match. Each item in `and` is either a simple expression (property/operator/values) or an `or` group. At most one `or` group is allowed per request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CompanyProfileSearchFilter]**](CompanyProfileSearchFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_search_filters import CompanyProfileSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileSearchFilters from a JSON string
company_profile_search_filters_instance = CompanyProfileSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileSearchFilters.to_json())

# convert the object into a dict
company_profile_search_filters_dict = company_profile_search_filters_instance.to_dict()
# create an instance of CompanyProfileSearchFilters from a dict
company_profile_search_filters_from_dict = CompanyProfileSearchFilters.from_dict(company_profile_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


