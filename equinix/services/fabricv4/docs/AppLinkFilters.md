# AppLinkFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppLinkFilter]**](AppLinkFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_filters import AppLinkFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkFilters from a JSON string
app_link_filters_instance = AppLinkFilters.from_json(json)
# print the JSON string representation of the object
print(AppLinkFilters.to_json())

# convert the object into a dict
app_link_filters_dict = app_link_filters_instance.to_dict()
# create an instance of AppLinkFilters from a dict
app_link_filters_from_dict = AppLinkFilters.from_dict(app_link_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


