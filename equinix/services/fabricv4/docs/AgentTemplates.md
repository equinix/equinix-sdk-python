# AgentTemplates

Agent Template object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Agent Template URI | [optional] 
**type** | **str** | type | [optional] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Equinix-provided agent template name | [optional] 
**description** | **str** | Equinix-provided agent template description | [optional] 
**state** | [**AgentTemplatesState**](AgentTemplatesState.md) |  | [optional] 
**enabled** | **bool** | Equinix-provided agent template enabled status | [optional] 
**agent_definition** | [**AgentDefinition**](AgentDefinition.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_templates import AgentTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTemplates from a JSON string
agent_templates_instance = AgentTemplates.from_json(json)
# print the JSON string representation of the object
print(AgentTemplates.to_json())

# convert the object into a dict
agent_templates_dict = agent_templates_instance.to_dict()
# create an instance of AgentTemplates from a dict
agent_templates_from_dict = AgentTemplates.from_dict(agent_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


