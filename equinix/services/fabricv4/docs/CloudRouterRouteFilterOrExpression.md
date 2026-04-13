# CloudRouterRouteFilterOrExpression

OR expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CloudRouterRouteFilterExpression]**](CloudRouterRouteFilterExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filter_or_expression import CloudRouterRouteFilterOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFilterOrExpression from a JSON string
cloud_router_route_filter_or_expression_instance = CloudRouterRouteFilterOrExpression.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFilterOrExpression.to_json())

# convert the object into a dict
cloud_router_route_filter_or_expression_dict = cloud_router_route_filter_or_expression_instance.to_dict()
# create an instance of CloudRouterRouteFilterOrExpression from a dict
cloud_router_route_filter_or_expression_from_dict = CloudRouterRouteFilterOrExpression.from_dict(cloud_router_route_filter_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


