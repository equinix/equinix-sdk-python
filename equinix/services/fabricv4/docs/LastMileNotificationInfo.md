# LastMileNotificationInfo

Last mile notification contact information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key | [optional] 
**value** | **str** | Value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.last_mile_notification_info import LastMileNotificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LastMileNotificationInfo from a JSON string
last_mile_notification_info_instance = LastMileNotificationInfo.from_json(json)
# print the JSON string representation of the object
print(LastMileNotificationInfo.to_json())

# convert the object into a dict
last_mile_notification_info_dict = last_mile_notification_info_instance.to_dict()
# create an instance of LastMileNotificationInfo from a dict
last_mile_notification_info_from_dict = LastMileNotificationInfo.from_dict(last_mile_notification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


