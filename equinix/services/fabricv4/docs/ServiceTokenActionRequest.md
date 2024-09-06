# ServiceTokenActionRequest

Service Token action request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceTokenActions**](ServiceTokenActions.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.service_token_action_request import ServiceTokenActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenActionRequest from a JSON string
service_token_action_request_instance = ServiceTokenActionRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenActionRequest.to_json())

# convert the object into a dict
service_token_action_request_dict = service_token_action_request_instance.to_dict()
# create an instance of ServiceTokenActionRequest from a dict
service_token_action_request_from_dict = ServiceTokenActionRequest.from_dict(service_token_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


