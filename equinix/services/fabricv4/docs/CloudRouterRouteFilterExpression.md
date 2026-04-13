# CloudRouterRouteFilterExpression

Filter expression that can be AND, OR, or a simple expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterRouteFilterExpression]**](CloudRouterRouteFilterExpression.md) |  | [optional] 
**var_or** | [**List[CloudRouterRouteFilterExpression]**](CloudRouterRouteFilterExpression.md) |  | [optional] 
**var_property** | [**CloudRouterRouteFilterSimpleExpressionProperty**](CloudRouterRouteFilterSimpleExpressionProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filter_expression import CloudRouterRouteFilterExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFilterExpression from a JSON string
cloud_router_route_filter_expression_instance = CloudRouterRouteFilterExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFilterExpression.to_json())

# convert the object into a dict
cloud_router_route_filter_expression_dict = cloud_router_route_filter_expression_instance.to_dict()
# create an instance of CloudRouterRouteFilterExpression from a dict
cloud_router_route_filter_expression_from_dict = CloudRouterRouteFilterExpression.from_dict(cloud_router_route_filter_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


