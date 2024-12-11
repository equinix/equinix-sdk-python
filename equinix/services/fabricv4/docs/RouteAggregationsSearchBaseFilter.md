# RouteAggregationsSearchBaseFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteAggregationsSearchFilterItem]**](RouteAggregationsSearchFilterItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_search_base_filter import RouteAggregationsSearchBaseFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsSearchBaseFilter from a JSON string
route_aggregations_search_base_filter_instance = RouteAggregationsSearchBaseFilter.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsSearchBaseFilter.to_json())

# convert the object into a dict
route_aggregations_search_base_filter_dict = route_aggregations_search_base_filter_instance.to_dict()
# create an instance of RouteAggregationsSearchBaseFilter from a dict
route_aggregations_search_base_filter_form_dict = route_aggregations_search_base_filter.from_dict(route_aggregations_search_base_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


