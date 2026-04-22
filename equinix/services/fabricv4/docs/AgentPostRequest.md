# AgentPostRequest

Create Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Customer-provided agent name | 
**description** | **str** | Customer-provided agent description | [optional] 
**enabled** | **bool** | Customer-provided agent enabled status | [optional] 
**project** | [**Project**](Project.md) |  | 
**agent_template** | [**AgentTemplate**](AgentTemplate.md) |  | 
**configuration** | [**Configuration**](Configuration.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_post_request import AgentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPostRequest from a JSON string
agent_post_request_instance = AgentPostRequest.from_json(json)
# print the JSON string representation of the object
print(AgentPostRequest.to_json())

# convert the object into a dict
agent_post_request_dict = agent_post_request_instance.to_dict()
# create an instance of AgentPostRequest from a dict
agent_post_request_from_dict = AgentPostRequest.from_dict(agent_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


