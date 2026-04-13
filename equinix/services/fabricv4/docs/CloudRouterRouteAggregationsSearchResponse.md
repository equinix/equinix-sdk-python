# CloudRouterRouteAggregationsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionRouteAggregationData]**](ConnectionRouteAggregationData.md) | List of route aggregation attachments for a given cloud router | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregations_search_response import CloudRouterRouteAggregationsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationsSearchResponse from a JSON string
cloud_router_route_aggregations_search_response_instance = CloudRouterRouteAggregationsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationsSearchResponse.to_json())

# convert the object into a dict
cloud_router_route_aggregations_search_response_dict = cloud_router_route_aggregations_search_response_instance.to_dict()
# create an instance of CloudRouterRouteAggregationsSearchResponse from a dict
cloud_router_route_aggregations_search_response_from_dict = CloudRouterRouteAggregationsSearchResponse.from_dict(cloud_router_route_aggregations_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


