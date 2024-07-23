# SimplifiedNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SimplifiedNotificationType**](SimplifiedNotificationType.md) |  | 
**send_interval** | **str** |  | [optional] 
**emails** | **List[str]** | Array of contact emails | 
**registered_users** | **List[str]** | Array of registered users | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_notification import SimplifiedNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedNotification from a JSON string
simplified_notification_instance = SimplifiedNotification.from_json(json)
# print the JSON string representation of the object
print(SimplifiedNotification.to_json())

# convert the object into a dict
simplified_notification_dict = simplified_notification_instance.to_dict()
# create an instance of SimplifiedNotification from a dict
simplified_notification_form_dict = simplified_notification.from_dict(simplified_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


