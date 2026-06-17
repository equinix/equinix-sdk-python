# RouteAggregationsSearchRequest

Search route aggregations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**SearchFilter**](SearchFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[RouteAggregationSortCriteria]**](RouteAggregationSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_search_request import RouteAggregationsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsSearchRequest from a JSON string
route_aggregations_search_request_instance = RouteAggregationsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsSearchRequest.to_json())

# convert the object into a dict
route_aggregations_search_request_dict = route_aggregations_search_request_instance.to_dict()
# create an instance of RouteAggregationsSearchRequest from a dict
route_aggregations_search_request_from_dict = RouteAggregationsSearchRequest.from_dict(route_aggregations_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


