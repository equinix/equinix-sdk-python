# CrossConnectResponseAllowedActions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CrossConnectActionType**](CrossConnectActionType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_response_allowed_actions import CrossConnectResponseAllowedActions

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectResponseAllowedActions from a JSON string
cross_connect_response_allowed_actions_instance = CrossConnectResponseAllowedActions.from_json(json)
# print the JSON string representation of the object
print(CrossConnectResponseAllowedActions.to_json())

# convert the object into a dict
cross_connect_response_allowed_actions_dict = cross_connect_response_allowed_actions_instance.to_dict()
# create an instance of CrossConnectResponseAllowedActions from a dict
cross_connect_response_allowed_actions_from_dict = CrossConnectResponseAllowedActions.from_dict(cross_connect_response_allowed_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


