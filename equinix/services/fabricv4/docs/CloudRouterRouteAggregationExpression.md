# CloudRouterRouteAggregationExpression

Filter expression that can be AND, OR, or a simple expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 
**var_or** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 
**var_property** | [**CloudRouterRouteAggregationSimpleExpressionProperty**](CloudRouterRouteAggregationSimpleExpressionProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregation_expression import CloudRouterRouteAggregationExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationExpression from a JSON string
cloud_router_route_aggregation_expression_instance = CloudRouterRouteAggregationExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationExpression.to_json())

# convert the object into a dict
cloud_router_route_aggregation_expression_dict = cloud_router_route_aggregation_expression_instance.to_dict()
# create an instance of CloudRouterRouteAggregationExpression from a dict
cloud_router_route_aggregation_expression_from_dict = CloudRouterRouteAggregationExpression.from_dict(cloud_router_route_aggregation_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


