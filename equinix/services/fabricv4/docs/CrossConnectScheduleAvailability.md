# CrossConnectScheduleAvailability

Cross Connect schedule window offered at an IBX.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Schedule URI. | [optional] [readonly] 
**type** | [**CrossConnectScheduleAvailabilityType**](CrossConnectScheduleAvailabilityType.md) |  | [optional] 
**code** | [**ScheduleType**](ScheduleType.md) |  | [optional] [readonly] 
**a_side** | [**CrossConnectScheduleAvailabilityASide**](CrossConnectScheduleAvailabilityASide.md) |  | [optional] 
**z_side** | [**CrossConnectScheduleAvailabilityZSide**](CrossConnectScheduleAvailabilityZSide.md) |  | [optional] 
**start_date_time** | **datetime** | Start of the schedule window. | [optional] [readonly] 
**end_date_time** | **datetime** | End of the schedule window. | [optional] [readonly] 
**unavailable_dates** | **List[date]** | Dates within the schedule window when the IBX is unavailable, such as the holidays observed at the IBX.  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_schedule_availability import CrossConnectScheduleAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectScheduleAvailability from a JSON string
cross_connect_schedule_availability_instance = CrossConnectScheduleAvailability.from_json(json)
# print the JSON string representation of the object
print(CrossConnectScheduleAvailability.to_json())

# convert the object into a dict
cross_connect_schedule_availability_dict = cross_connect_schedule_availability_instance.to_dict()
# create an instance of CrossConnectScheduleAvailability from a dict
cross_connect_schedule_availability_from_dict = CrossConnectScheduleAvailability.from_dict(cross_connect_schedule_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


