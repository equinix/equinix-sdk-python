# RouteAggregationsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationsData]**](RouteAggregationsData.md) | List of Route Aggregations | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_search_response import RouteAggregationsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsSearchResponse from a JSON string
route_aggregations_search_response_instance = RouteAggregationsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsSearchResponse.to_json())

# convert the object into a dict
route_aggregations_search_response_dict = route_aggregations_search_response_instance.to_dict()
# create an instance of RouteAggregationsSearchResponse from a dict
route_aggregations_search_response_from_dict = RouteAggregationsSearchResponse.from_dict(route_aggregations_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


