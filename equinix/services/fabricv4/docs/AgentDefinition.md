# AgentDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Agent Template ReadMe (.md) Definition | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_definition import AgentDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDefinition from a JSON string
agent_definition_instance = AgentDefinition.from_json(json)
# print the JSON string representation of the object
print(AgentDefinition.to_json())

# convert the object into a dict
agent_definition_dict = agent_definition_instance.to_dict()
# create an instance of AgentDefinition from a dict
agent_definition_from_dict = AgentDefinition.from_dict(agent_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


