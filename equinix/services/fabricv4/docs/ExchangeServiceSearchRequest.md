# ExchangeServiceSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ExchangeServiceSearchExpression**](ExchangeServiceSearchExpression.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[ExchangeServiceSearchSortCriteria]**](ExchangeServiceSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_search_request import ExchangeServiceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceSearchRequest from a JSON string
exchange_service_search_request_instance = ExchangeServiceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceSearchRequest.to_json())

# convert the object into a dict
exchange_service_search_request_dict = exchange_service_search_request_instance.to_dict()
# create an instance of ExchangeServiceSearchRequest from a dict
exchange_service_search_request_from_dict = ExchangeServiceSearchRequest.from_dict(exchange_service_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


