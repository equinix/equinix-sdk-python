# PortNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PortNotificationType**](PortNotificationType.md) |  | 
**registered_users** | **List[str]** | Array of registered users | 

## Example

```python
from equinix.services.fabricv4.models.port_notification import PortNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PortNotification from a JSON string
port_notification_instance = PortNotification.from_json(json)
# print the JSON string representation of the object
print(PortNotification.to_json())

# convert the object into a dict
port_notification_dict = port_notification_instance.to_dict()
# create an instance of PortNotification from a dict
port_notification_from_dict = PortNotification.from_dict(port_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


