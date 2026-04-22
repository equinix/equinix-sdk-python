# CloudRouterRouteAggregationOrExpression

OR expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregation_or_expression import CloudRouterRouteAggregationOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationOrExpression from a JSON string
cloud_router_route_aggregation_or_expression_instance = CloudRouterRouteAggregationOrExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationOrExpression.to_json())

# convert the object into a dict
cloud_router_route_aggregation_or_expression_dict = cloud_router_route_aggregation_or_expression_instance.to_dict()
# create an instance of CloudRouterRouteAggregationOrExpression from a dict
cloud_router_route_aggregation_or_expression_from_dict = CloudRouterRouteAggregationOrExpression.from_dict(cloud_router_route_aggregation_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


