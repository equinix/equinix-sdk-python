# RouteFiltersSearchBaseFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteFiltersSearchFilterItem]**](RouteFiltersSearchFilterItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_search_base_filter import RouteFiltersSearchBaseFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersSearchBaseFilter from a JSON string
route_filters_search_base_filter_instance = RouteFiltersSearchBaseFilter.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersSearchBaseFilter.to_json())

# convert the object into a dict
route_filters_search_base_filter_dict = route_filters_search_base_filter_instance.to_dict()
# create an instance of RouteFiltersSearchBaseFilter from a dict
route_filters_search_base_filter_form_dict = route_filters_search_base_filter.from_dict(route_filters_search_base_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


