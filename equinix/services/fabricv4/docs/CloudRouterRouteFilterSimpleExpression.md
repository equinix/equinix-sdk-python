# CloudRouterRouteFilterSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CloudRouterRouteFilterSimpleExpressionProperty**](CloudRouterRouteFilterSimpleExpressionProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filter_simple_expression import CloudRouterRouteFilterSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFilterSimpleExpression from a JSON string
cloud_router_route_filter_simple_expression_instance = CloudRouterRouteFilterSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFilterSimpleExpression.to_json())

# convert the object into a dict
cloud_router_route_filter_simple_expression_dict = cloud_router_route_filter_simple_expression_instance.to_dict()
# create an instance of CloudRouterRouteFilterSimpleExpression from a dict
cloud_router_route_filter_simple_expression_from_dict = CloudRouterRouteFilterSimpleExpression.from_dict(cloud_router_route_filter_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


