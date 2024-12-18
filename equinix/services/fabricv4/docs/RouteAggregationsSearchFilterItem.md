# RouteAggregationsSearchFilterItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**RouteFiltersSearchFilterItemProperty**](RouteFiltersSearchFilterItemProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_search_filter_item import RouteAggregationsSearchFilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsSearchFilterItem from a JSON string
route_aggregations_search_filter_item_instance = RouteAggregationsSearchFilterItem.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsSearchFilterItem.to_json())

# convert the object into a dict
route_aggregations_search_filter_item_dict = route_aggregations_search_filter_item_instance.to_dict()
# create an instance of RouteAggregationsSearchFilterItem from a dict
route_aggregations_search_filter_item_form_dict = route_aggregations_search_filter_item.from_dict(route_aggregations_search_filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


