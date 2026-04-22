# AgentTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Agent Template Uuid | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_template import AgentTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTemplate from a JSON string
agent_template_instance = AgentTemplate.from_json(json)
# print the JSON string representation of the object
print(AgentTemplate.to_json())

# convert the object into a dict
agent_template_dict = agent_template_instance.to_dict()
# create an instance of AgentTemplate from a dict
agent_template_from_dict = AgentTemplate.from_dict(agent_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


