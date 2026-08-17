# AppDomainFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppDomainFilter]**](AppDomainFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_filters import AppDomainFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainFilters from a JSON string
app_domain_filters_instance = AppDomainFilters.from_json(json)
# print the JSON string representation of the object
print(AppDomainFilters.to_json())

# convert the object into a dict
app_domain_filters_dict = app_domain_filters_instance.to_dict()
# create an instance of AppDomainFilters from a dict
app_domain_filters_from_dict = AppDomainFilters.from_dict(app_domain_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


