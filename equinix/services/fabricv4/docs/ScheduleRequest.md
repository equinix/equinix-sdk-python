# ScheduleRequest

Cross Connect Installation Schedule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScheduleRequestType**](ScheduleRequestType.md) |  | [optional] 
**code** | [**ScheduleType**](ScheduleType.md) |  | 
**auto_convert_to_standard** | **bool** | Applicable only when the code is EXPEDITE. When true, Equinix schedules the Cross Connect as STANDARD when no EXPEDITE scheduling is available.  | [optional] 
**readiness_date_time** | **datetime** | Carrier Circuit delivery date is the date when the Carrier commits to enable the circuit. Your order will be placed on hold, pending the date you enter. Equinix will wait for the Carrier to deliver the service and then will complete the installation.  | [optional] 
**requested_date_time** | **datetime** | Requested Installation Date and Time. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.schedule_request import ScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleRequest from a JSON string
schedule_request_instance = ScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleRequest.to_json())

# convert the object into a dict
schedule_request_dict = schedule_request_instance.to_dict()
# create an instance of ScheduleRequest from a dict
schedule_request_from_dict = ScheduleRequest.from_dict(schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


