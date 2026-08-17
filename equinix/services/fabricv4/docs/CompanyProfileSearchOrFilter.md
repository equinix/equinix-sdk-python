# CompanyProfileSearchOrFilter

Groups multiple simple expressions with OR logic. At most one `or` group is allowed within the top-level `and` array. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CompanyProfileSearchSimpleExpression]**](CompanyProfileSearchSimpleExpression.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.company_profile_search_or_filter import CompanyProfileSearchOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyProfileSearchOrFilter from a JSON string
company_profile_search_or_filter_instance = CompanyProfileSearchOrFilter.from_json(json)
# print the JSON string representation of the object
print(CompanyProfileSearchOrFilter.to_json())

# convert the object into a dict
company_profile_search_or_filter_dict = company_profile_search_or_filter_instance.to_dict()
# create an instance of CompanyProfileSearchOrFilter from a dict
company_profile_search_or_filter_from_dict = CompanyProfileSearchOrFilter.from_dict(company_profile_search_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


