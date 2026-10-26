# ExchangeServiceActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExchangeServiceActionRequestType**](ExchangeServiceActionRequestType.md) |  | 
**href** | **str** | Internet Exchange Service Action URI | [optional] 
**uuid** | **str** | Action identifier | [optional] 
**description** | **str** | Action description | [optional] 
**state** | [**ExchangeServiceActionResponseAllOfState**](ExchangeServiceActionResponseAllOfState.md) |  | [optional] 
**changelog** | [**PlatformChangelog**](PlatformChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_action_response import ExchangeServiceActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceActionResponse from a JSON string
exchange_service_action_response_instance = ExchangeServiceActionResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceActionResponse.to_json())

# convert the object into a dict
exchange_service_action_response_dict = exchange_service_action_response_instance.to_dict()
# create an instance of ExchangeServiceActionResponse from a dict
exchange_service_action_response_from_dict = ExchangeServiceActionResponse.from_dict(exchange_service_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


