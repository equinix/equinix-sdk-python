# RouteAggregationsSearchBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**RouteAggregationsSearchBaseFilter**](RouteAggregationsSearchBaseFilter.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[RouteAggregationSortItem]**](RouteAggregationSortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_search_base import RouteAggregationsSearchBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsSearchBase from a JSON string
route_aggregations_search_base_instance = RouteAggregationsSearchBase.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsSearchBase.to_json())

# convert the object into a dict
route_aggregations_search_base_dict = route_aggregations_search_base_instance.to_dict()
# create an instance of RouteAggregationsSearchBase from a dict
route_aggregations_search_base_form_dict = route_aggregations_search_base.from_dict(route_aggregations_search_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


