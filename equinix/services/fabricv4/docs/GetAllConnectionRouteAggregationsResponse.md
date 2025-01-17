# GetAllConnectionRouteAggregationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionRouteAggregationData]**](ConnectionRouteAggregationData.md) | List of Route Aggregations attached to a Connection | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_connection_route_aggregations_response import GetAllConnectionRouteAggregationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllConnectionRouteAggregationsResponse from a JSON string
get_all_connection_route_aggregations_response_instance = GetAllConnectionRouteAggregationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllConnectionRouteAggregationsResponse.to_json())

# convert the object into a dict
get_all_connection_route_aggregations_response_dict = get_all_connection_route_aggregations_response_instance.to_dict()
# create an instance of GetAllConnectionRouteAggregationsResponse from a dict
get_all_connection_route_aggregations_response_from_dict = GetAllConnectionRouteAggregationsResponse.from_dict(get_all_connection_route_aggregations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


