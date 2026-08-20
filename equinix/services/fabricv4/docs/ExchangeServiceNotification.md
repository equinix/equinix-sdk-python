# ExchangeServiceNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ExchangeServiceNotificationType**](ExchangeServiceNotificationType.md) |  | 
**registered_users** | **List[str]** | Array of registered users | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_notification import ExchangeServiceNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceNotification from a JSON string
exchange_service_notification_instance = ExchangeServiceNotification.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceNotification.to_json())

# convert the object into a dict
exchange_service_notification_dict = exchange_service_notification_instance.to_dict()
# create an instance of ExchangeServiceNotification from a dict
exchange_service_notification_from_dict = ExchangeServiceNotification.from_dict(exchange_service_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


