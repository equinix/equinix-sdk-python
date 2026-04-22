# Agents

Agent object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Agent URI | [optional] [readonly] 
**type** | **str** | type | [optional] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided agent name | [optional] 
**description** | **str** | Customer-provided agent description | [optional] 
**state** | [**AgentTemplatesState**](AgentTemplatesState.md) |  | [optional] 
**enabled** | **bool** | Customer-provided agent enabled status | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**agent_template** | [**AgentTemplate**](AgentTemplate.md) |  | [optional] 
**configuration** | [**Configuration**](Configuration.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agents import Agents

# TODO update the JSON string below
json = "{}"
# create an instance of Agents from a JSON string
agents_instance = Agents.from_json(json)
# print the JSON string representation of the object
print(Agents.to_json())

# convert the object into a dict
agents_dict = agents_instance.to_dict()
# create an instance of Agents from a dict
agents_from_dict = Agents.from_dict(agents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


