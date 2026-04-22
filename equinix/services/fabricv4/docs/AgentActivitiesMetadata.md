# AgentActivitiesMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_message** | [**ChatMessage**](ChatMessage.md) |  | [optional] 
**tool_call_information** | [**List[ToolCallInformationInner]**](ToolCallInformationInner.md) | List of tools called during the agent operation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_activities_metadata import AgentActivitiesMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AgentActivitiesMetadata from a JSON string
agent_activities_metadata_instance = AgentActivitiesMetadata.from_json(json)
# print the JSON string representation of the object
print(AgentActivitiesMetadata.to_json())

# convert the object into a dict
agent_activities_metadata_dict = agent_activities_metadata_instance.to_dict()
# create an instance of AgentActivitiesMetadata from a dict
agent_activities_metadata_from_dict = AgentActivitiesMetadata.from_dict(agent_activities_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


