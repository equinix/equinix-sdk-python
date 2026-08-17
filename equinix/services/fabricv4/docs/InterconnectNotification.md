# InterconnectNotification

Interconnect notification preference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InterconnectNotificationType**](InterconnectNotificationType.md) |  | [optional] 
**emails** | **List[str]** | Array of contact emails | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_notification import InterconnectNotification

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectNotification from a JSON string
interconnect_notification_instance = InterconnectNotification.from_json(json)
# print the JSON string representation of the object
print(InterconnectNotification.to_json())

# convert the object into a dict
interconnect_notification_dict = interconnect_notification_instance.to_dict()
# create an instance of InterconnectNotification from a dict
interconnect_notification_from_dict = InterconnectNotification.from_dict(interconnect_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


