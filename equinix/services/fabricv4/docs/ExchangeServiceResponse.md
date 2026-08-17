# ExchangeServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Internet Exchange Service URI | [optional] 
**uuid** | **str** | Internet Exchange Service identifier | [optional] 
**type** | [**ExchangeServiceResponseType**](ExchangeServiceResponseType.md) |  | [optional] [default to ExchangeServiceResponseType.IX]
**name** | **str** | Name | [optional] 
**bandwidth** | **int** | bandwidth in Mbps | [optional] 
**description** | **str** | Description | [optional] 
**state** | [**ExchangeServiceResponseState**](ExchangeServiceResponseState.md) |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**public_peering_connection** | [**PublicPeeringConnectionResponse**](PublicPeeringConnectionResponse.md) |  | [optional] 
**routing_protocol** | [**RoutingProtocolResponse**](RoutingProtocolResponse.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[ExchangeServiceNotification]**](ExchangeServiceNotification.md) | Preferences for notifications on Internet Exchange Service configuration or status changes | [optional] 
**changelog** | [**PlatformChangelog**](PlatformChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_response import ExchangeServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceResponse from a JSON string
exchange_service_response_instance = ExchangeServiceResponse.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceResponse.to_json())

# convert the object into a dict
exchange_service_response_dict = exchange_service_response_instance.to_dict()
# create an instance of ExchangeServiceResponse from a dict
exchange_service_response_from_dict = ExchangeServiceResponse.from_dict(exchange_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


