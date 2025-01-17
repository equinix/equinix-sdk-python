# ConnectionAction

Connection action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Actions**](Actions.md) |  | 
**href** | **str** | Connection action URI | [readonly] 
**uuid** | **str** | Equinix-assigned connection identifier | 
**description** | **str** | Connection rejection reason detail | [optional] 
**data** | [**ConnectionAcceptanceData**](ConnectionAcceptanceData.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_action import ConnectionAction

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionAction from a JSON string
connection_action_instance = ConnectionAction.from_json(json)
# print the JSON string representation of the object
print(ConnectionAction.to_json())

# convert the object into a dict
connection_action_dict = connection_action_instance.to_dict()
# create an instance of ConnectionAction from a dict
connection_action_from_dict = ConnectionAction.from_dict(connection_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


