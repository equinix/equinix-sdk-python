# CrossConnectResponseAllowedActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CrossConnectActionType**](CrossConnectActionType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_response_allowed_actions_inner import CrossConnectResponseAllowedActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectResponseAllowedActionsInner from a JSON string
cross_connect_response_allowed_actions_inner_instance = CrossConnectResponseAllowedActionsInner.from_json(json)
# print the JSON string representation of the object
print(CrossConnectResponseAllowedActionsInner.to_json())

# convert the object into a dict
cross_connect_response_allowed_actions_inner_dict = cross_connect_response_allowed_actions_inner_instance.to_dict()
# create an instance of CrossConnectResponseAllowedActionsInner from a dict
cross_connect_response_allowed_actions_inner_from_dict = CrossConnectResponseAllowedActionsInner.from_dict(cross_connect_response_allowed_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


