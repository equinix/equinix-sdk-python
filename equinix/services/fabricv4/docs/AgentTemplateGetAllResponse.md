# AgentTemplateGetAllResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AgentTemplates]**](AgentTemplates.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_template_get_all_response import AgentTemplateGetAllResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTemplateGetAllResponse from a JSON string
agent_template_get_all_response_instance = AgentTemplateGetAllResponse.from_json(json)
# print the JSON string representation of the object
print(AgentTemplateGetAllResponse.to_json())

# convert the object into a dict
agent_template_get_all_response_dict = agent_template_get_all_response_instance.to_dict()
# create an instance of AgentTemplateGetAllResponse from a dict
agent_template_get_all_response_from_dict = AgentTemplateGetAllResponse.from_dict(agent_template_get_all_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


