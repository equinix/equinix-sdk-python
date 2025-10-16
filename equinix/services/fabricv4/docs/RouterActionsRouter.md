# RouterActionsRouter

Router object for router actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Router UUID | [optional] 
**href** | **str** |  | [optional] 
**type** | [**CloudRouterPostRequestBaseType**](CloudRouterPostRequestBaseType.md) |  | [optional] 
**operation** | [**Operation**](Operation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.router_actions_router import RouterActionsRouter

# TODO update the JSON string below
json = "{}"
# create an instance of RouterActionsRouter from a JSON string
router_actions_router_instance = RouterActionsRouter.from_json(json)
# print the JSON string representation of the object
print(RouterActionsRouter.to_json())

# convert the object into a dict
router_actions_router_dict = router_actions_router_instance.to_dict()
# create an instance of RouterActionsRouter from a dict
router_actions_router_from_dict = RouterActionsRouter.from_dict(router_actions_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


