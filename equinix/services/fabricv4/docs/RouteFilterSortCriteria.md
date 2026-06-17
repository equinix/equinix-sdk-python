# RouteFilterSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**RouteFilterSortDirection**](RouteFilterSortDirection.md) |  | [optional] [default to RouteFilterSortDirection.DESC]
**var_property** | [**RouteFilterSortBy**](RouteFilterSortBy.md) |  | [optional] [default to RouteFilterSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.route_filter_sort_criteria import RouteFilterSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterSortCriteria from a JSON string
route_filter_sort_criteria_instance = RouteFilterSortCriteria.from_json(json)
# print the JSON string representation of the object
print(RouteFilterSortCriteria.to_json())

# convert the object into a dict
route_filter_sort_criteria_dict = route_filter_sort_criteria_instance.to_dict()
# create an instance of RouteFilterSortCriteria from a dict
route_filter_sort_criteria_from_dict = RouteFilterSortCriteria.from_dict(route_filter_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


