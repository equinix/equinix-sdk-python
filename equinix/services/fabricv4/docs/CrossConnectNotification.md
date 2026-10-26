# CrossConnectNotification

Cross Connect Notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) |  | 
**first_name** | **str** | First name of the unregistered contact. Applicable only to the TECHNICAL_UNREGISTERED type.  | [optional] 
**last_name** | **str** | Last name of the unregistered contact. Applicable only to the TECHNICAL_UNREGISTERED type.  | [optional] 
**emails** | **List[str]** | Email addresses for notifications. | 
**registered_users** | **List[str]** | Registered users for notifications. | [optional] 
**phone** | [**List[CrossConnectPhone]**](CrossConnectPhone.md) | Contact phone numbers. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_notification import CrossConnectNotification

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectNotification from a JSON string
cross_connect_notification_instance = CrossConnectNotification.from_json(json)
# print the JSON string representation of the object
print(CrossConnectNotification.to_json())

# convert the object into a dict
cross_connect_notification_dict = cross_connect_notification_instance.to_dict()
# create an instance of CrossConnectNotification from a dict
cross_connect_notification_from_dict = CrossConnectNotification.from_dict(cross_connect_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


