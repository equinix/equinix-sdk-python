# ExchangeServiceSearchResponse

List of Internet Exchange Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[ExchangeServiceSearchSortCriteria]**](ExchangeServiceSearchSortCriteria.md) |  | [optional] 
**data** | [**List[ExchangeServiceResponse]**](ExchangeServiceResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_search_response import ExchangeServiceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceSearchResponse from a JSON string
exchange_service_search_response_instance = ExchangeServiceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceSearchResponse.to_json())

# convert the object into a dict
exchange_service_search_response_dict = exchange_service_search_response_instance.to_dict()
# create an instance of ExchangeServiceSearchResponse from a dict
exchange_service_search_response_from_dict = ExchangeServiceSearchResponse.from_dict(exchange_service_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


