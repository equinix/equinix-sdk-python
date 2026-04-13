# CloudRouterRouteAggregationsFilter

Top-level filter that can be either an AND expression or OR expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 
**var_or** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregations_filter import CloudRouterRouteAggregationsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationsFilter from a JSON string
cloud_router_route_aggregations_filter_instance = CloudRouterRouteAggregationsFilter.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationsFilter.to_json())

# convert the object into a dict
cloud_router_route_aggregations_filter_dict = cloud_router_route_aggregations_filter_instance.to_dict()
# create an instance of CloudRouterRouteAggregationsFilter from a dict
cloud_router_route_aggregations_filter_from_dict = CloudRouterRouteAggregationsFilter.from_dict(cloud_router_route_aggregations_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


