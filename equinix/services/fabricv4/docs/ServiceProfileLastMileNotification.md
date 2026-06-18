# ServiceProfileLastMileNotification

Last-mile notification contact details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Expected format of the contact information, such as email or phone number. | [optional] 
**label** | **str** | Type of contact information, such as ordering or technical support. | [optional] 
**required** | **bool** | Whether this contact information is required for provisioning and ordering. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_last_mile_notification import ServiceProfileLastMileNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLastMileNotification from a JSON string
service_profile_last_mile_notification_instance = ServiceProfileLastMileNotification.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLastMileNotification.to_json())

# convert the object into a dict
service_profile_last_mile_notification_dict = service_profile_last_mile_notification_instance.to_dict()
# create an instance of ServiceProfileLastMileNotification from a dict
service_profile_last_mile_notification_from_dict = ServiceProfileLastMileNotification.from_dict(service_profile_last_mile_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


