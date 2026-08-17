# AppServiceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppServiceFilter]**](AppServiceFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_filters import AppServiceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceFilters from a JSON string
app_service_filters_instance = AppServiceFilters.from_json(json)
# print the JSON string representation of the object
print(AppServiceFilters.to_json())

# convert the object into a dict
app_service_filters_dict = app_service_filters_instance.to_dict()
# create an instance of AppServiceFilters from a dict
app_service_filters_from_dict = AppServiceFilters.from_dict(app_service_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


