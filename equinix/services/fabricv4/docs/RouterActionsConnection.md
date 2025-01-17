# RouterActionsConnection

Connection object for router actions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Connection UUID | [optional] 

## Example

```python
from equinix.services.fabricv4.models.router_actions_connection import RouterActionsConnection

# TODO update the JSON string below
json = "{}"
# create an instance of RouterActionsConnection from a JSON string
router_actions_connection_instance = RouterActionsConnection.from_json(json)
# print the JSON string representation of the object
print(RouterActionsConnection.to_json())

# convert the object into a dict
router_actions_connection_dict = router_actions_connection_instance.to_dict()
# create an instance of RouterActionsConnection from a dict
router_actions_connection_from_dict = RouterActionsConnection.from_dict(router_actions_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


