# AgentGetAllResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Agents]**](Agents.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.agent_get_all_response import AgentGetAllResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGetAllResponse from a JSON string
agent_get_all_response_instance = AgentGetAllResponse.from_json(json)
# print the JSON string representation of the object
print(AgentGetAllResponse.to_json())

# convert the object into a dict
agent_get_all_response_dict = agent_get_all_response_instance.to_dict()
# create an instance of AgentGetAllResponse from a dict
agent_get_all_response_from_dict = AgentGetAllResponse.from_dict(agent_get_all_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


