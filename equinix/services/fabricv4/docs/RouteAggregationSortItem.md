# RouteAggregationSortItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**RouteAggregationSortItemProperty**](RouteAggregationSortItemProperty.md) |  | [optional] [default to RouteAggregationSortItemProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]
**direction** | [**SortItemDirection**](SortItemDirection.md) |  | [optional] [default to SortItemDirection.DESC]

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_sort_item import RouteAggregationSortItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationSortItem from a JSON string
route_aggregation_sort_item_instance = RouteAggregationSortItem.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationSortItem.to_json())

# convert the object into a dict
route_aggregation_sort_item_dict = route_aggregation_sort_item_instance.to_dict()
# create an instance of RouteAggregationSortItem from a dict
route_aggregation_sort_item_from_dict = RouteAggregationSortItem.from_dict(route_aggregation_sort_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


