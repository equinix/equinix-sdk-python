# ServiceTokenSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ServiceTokenSearchExpression**](ServiceTokenSearchExpression.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_token_search_request import ServiceTokenSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenSearchRequest from a JSON string
service_token_search_request_instance = ServiceTokenSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenSearchRequest.to_json())

# convert the object into a dict
service_token_search_request_dict = service_token_search_request_instance.to_dict()
# create an instance of ServiceTokenSearchRequest from a dict
service_token_search_request_from_dict = ServiceTokenSearchRequest.from_dict(service_token_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


