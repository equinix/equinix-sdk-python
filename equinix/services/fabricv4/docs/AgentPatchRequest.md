# AgentPatchRequest

Update Agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | path inside document leading to updated parameters for /name, /description, /enabled, and /configration/prompt | 
**op** | **str** | Handy shortcut for operation name | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.agent_patch_request import AgentPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPatchRequest from a JSON string
agent_patch_request_instance = AgentPatchRequest.from_json(json)
# print the JSON string representation of the object
print(AgentPatchRequest.to_json())

# convert the object into a dict
agent_patch_request_dict = agent_patch_request_instance.to_dict()
# create an instance of AgentPatchRequest from a dict
agent_patch_request_from_dict = AgentPatchRequest.from_dict(agent_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


