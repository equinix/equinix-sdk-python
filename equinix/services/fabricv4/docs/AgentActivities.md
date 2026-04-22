# AgentActivities

Agent Activities object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Agent Activities URI | [optional] 
**type** | **str** | type | [optional] 
**uuid** | **str** | Equinix-assigned agent operation identifier | [optional] [readonly] 
**agent** | [**Agent**](Agent.md) |  | [optional] 
**status** | **str** | Agent activities state COMPLETED, PENDING, PENDING_USER_INPUT, FAILED | [optional] 
**metadata** | [**AgentActivitiesMetadata**](AgentActivitiesMetadata.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_activities import AgentActivities

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivities from a JSON string
agent_activities_instance = AgentActivities.from_json(json)
# print the JSON string representation of the object
print(AgentActivities.to_json())

# convert the object into a dict
agent_activities_dict = agent_activities_instance.to_dict()
# create an instance of AgentActivities from a dict
agent_activities_from_dict = AgentActivities.from_dict(agent_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


