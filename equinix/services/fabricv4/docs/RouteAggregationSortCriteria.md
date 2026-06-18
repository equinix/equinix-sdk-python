# RouteAggregationSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**RouteAggregationSortDirection**](RouteAggregationSortDirection.md) |  | [optional] [default to RouteAggregationSortDirection.DESC]
**var_property** | [**RouteAggregationSortBy**](RouteAggregationSortBy.md) |  | [optional] [default to RouteAggregationSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_sort_criteria import RouteAggregationSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationSortCriteria from a JSON string
route_aggregation_sort_criteria_instance = RouteAggregationSortCriteria.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationSortCriteria.to_json())

# convert the object into a dict
route_aggregation_sort_criteria_dict = route_aggregation_sort_criteria_instance.to_dict()
# create an instance of RouteAggregationSortCriteria from a dict
route_aggregation_sort_criteria_from_dict = RouteAggregationSortCriteria.from_dict(route_aggregation_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


