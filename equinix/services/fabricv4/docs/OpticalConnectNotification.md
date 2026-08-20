# OpticalConnectNotification

Notification preferences for this connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OpticalConnectNotificationType**](OpticalConnectNotificationType.md) |  | 
**emails** | **List[str]** | Email addresses to notify. | 
**registered_users** | **List[str]** | Usernames of registered Equinix Portal users to notify. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_notification import OpticalConnectNotification

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectNotification from a JSON string
optical_connect_notification_instance = OpticalConnectNotification.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectNotification.to_json())

# convert the object into a dict
optical_connect_notification_dict = optical_connect_notification_instance.to_dict()
# create an instance of OpticalConnectNotification from a dict
optical_connect_notification_from_dict = OpticalConnectNotification.from_dict(optical_connect_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


