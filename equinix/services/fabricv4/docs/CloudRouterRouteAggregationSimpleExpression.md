# CloudRouterRouteAggregationSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CloudRouterRouteAggregationSimpleExpressionProperty**](CloudRouterRouteAggregationSimpleExpressionProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregation_simple_expression import CloudRouterRouteAggregationSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationSimpleExpression from a JSON string
cloud_router_route_aggregation_simple_expression_instance = CloudRouterRouteAggregationSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationSimpleExpression.to_json())

# convert the object into a dict
cloud_router_route_aggregation_simple_expression_dict = cloud_router_route_aggregation_simple_expression_instance.to_dict()
# create an instance of CloudRouterRouteAggregationSimpleExpression from a dict
cloud_router_route_aggregation_simple_expression_from_dict = CloudRouterRouteAggregationSimpleExpression.from_dict(cloud_router_route_aggregation_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


