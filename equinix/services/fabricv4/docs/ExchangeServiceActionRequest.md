# ExchangeServiceActionRequest

Internet Exchange Service Action Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExchangeServiceActionRequestType**](ExchangeServiceActionRequestType.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_action_request import ExchangeServiceActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceActionRequest from a JSON string
exchange_service_action_request_instance = ExchangeServiceActionRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceActionRequest.to_json())

# convert the object into a dict
exchange_service_action_request_dict = exchange_service_action_request_instance.to_dict()
# create an instance of ExchangeServiceActionRequest from a dict
exchange_service_action_request_from_dict = ExchangeServiceActionRequest.from_dict(exchange_service_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


