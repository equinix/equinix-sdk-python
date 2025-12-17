# CompanyProfileSearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CompanyProfileSearchFilter]**](CompanyProfileSearchFilter.md) |  | [optional] 
**var_or** | [**List[CompanyProfileSearchFilter]**](CompanyProfileSearchFilter.md) |  | [optional] 
**var_property** | **str** | Searchable field names in company profile | [optional] 
**operator** | **str** | Comparison operators for filtering | [optional] 
**values** | **List[str]** | Values to compare against | [optional] 

## Example

```python
from equinix.services.fabricv4.models.company_profile_search_filter import CompanyProfileSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileSearchFilter from a JSON string
company_profile_search_filter_instance = CompanyProfileSearchFilter.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileSearchFilter.to_json())

# convert the object into a dict
company_profile_search_filter_dict = company_profile_search_filter_instance.to_dict()
# create an instance of CompanyProfileSearchFilter from a dict
company_profile_search_filter_from_dict = CompanyProfileSearchFilter.from_dict(company_profile_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


