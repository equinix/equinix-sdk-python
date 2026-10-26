# DeinstallScheduleRequest

Cross Connect Deinstallation Schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeinstallScheduleRequestType**](DeinstallScheduleRequestType.md) |  | [optional] 
**code** | [**DeinstallScheduleRequestCode**](DeinstallScheduleRequestCode.md) |  | [optional] [default to DeinstallScheduleRequestCode.STANDARD]
**requested_date_time** | **datetime** | Requested Removal Date and Time. | 
**deinstallation_date_time** | **datetime** | Deinstallation Date and Time. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.deinstall_schedule_request import DeinstallScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeinstallScheduleRequest from a JSON string
deinstall_schedule_request_instance = DeinstallScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(DeinstallScheduleRequest.to_json())

# convert the object into a dict
deinstall_schedule_request_dict = deinstall_schedule_request_instance.to_dict()
# create an instance of DeinstallScheduleRequest from a dict
deinstall_schedule_request_from_dict = DeinstallScheduleRequest.from_dict(deinstall_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


