# AgentGetActivities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AgentActivities]**](AgentActivities.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_get_activities import AgentGetActivities

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetActivities from a JSON string
agent_get_activities_instance = AgentGetActivities.from_json(json)
# print the JSON string representation of the object
print(AgentGetActivities.to_json())

# convert the object into a dict
agent_get_activities_dict = agent_get_activities_instance.to_dict()
# create an instance of AgentGetActivities from a dict
agent_get_activities_from_dict = AgentGetActivities.from_dict(agent_get_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


