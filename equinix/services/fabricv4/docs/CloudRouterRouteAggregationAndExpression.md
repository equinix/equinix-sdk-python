# CloudRouterRouteAggregationAndExpression

AND expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterRouteAggregationExpression]**](CloudRouterRouteAggregationExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregation_and_expression import CloudRouterRouteAggregationAndExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationAndExpression from a JSON string
cloud_router_route_aggregation_and_expression_instance = CloudRouterRouteAggregationAndExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationAndExpression.to_json())

# convert the object into a dict
cloud_router_route_aggregation_and_expression_dict = cloud_router_route_aggregation_and_expression_instance.to_dict()
# create an instance of CloudRouterRouteAggregationAndExpression from a dict
cloud_router_route_aggregation_and_expression_from_dict = CloudRouterRouteAggregationAndExpression.from_dict(cloud_router_route_aggregation_and_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


