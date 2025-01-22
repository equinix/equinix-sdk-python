# GetRouteAggregationGetConnectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationConnectionsData]**](RouteAggregationConnectionsData.md) | List of Connections using a Route Aggregation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_route_aggregation_get_connections_response import GetRouteAggregationGetConnectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteAggregationGetConnectionsResponse from a JSON string
get_route_aggregation_get_connections_response_instance = GetRouteAggregationGetConnectionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRouteAggregationGetConnectionsResponse.to_json())

# convert the object into a dict
get_route_aggregation_get_connections_response_dict = get_route_aggregation_get_connections_response_instance.to_dict()
# create an instance of GetRouteAggregationGetConnectionsResponse from a dict
get_route_aggregation_get_connections_response_from_dict = GetRouteAggregationGetConnectionsResponse.from_dict(get_route_aggregation_get_connections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


