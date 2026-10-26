# ExchangeServiceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExchangeServiceCreateRequestType**](ExchangeServiceCreateRequestType.md) |  | 
**name** | **str** | Customer-provided internet exchange service name | 
**description** | **str** | Customer-provided internet exchange service description | [optional] 
**public_peering_connection** | [**PublicPeeringConnectionRequest**](PublicPeeringConnectionRequest.md) |  | 
**routing_protocol** | [**RoutingProtocolRequest**](RoutingProtocolRequest.md) |  | 
**order** | [**ExchangeServiceOrder**](ExchangeServiceOrder.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[ExchangeServiceNotification]**](ExchangeServiceNotification.md) | Preferences for notifications on Internet Exchange Service configuration or status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_create_request import ExchangeServiceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceCreateRequest from a JSON string
exchange_service_create_request_instance = ExchangeServiceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceCreateRequest.to_json())

# convert the object into a dict
exchange_service_create_request_dict = exchange_service_create_request_instance.to_dict()
# create an instance of ExchangeServiceCreateRequest from a dict
exchange_service_create_request_from_dict = ExchangeServiceCreateRequest.from_dict(exchange_service_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


