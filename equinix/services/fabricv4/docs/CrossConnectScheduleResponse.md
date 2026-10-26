# CrossConnectScheduleResponse

Schedule of a Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Schedule URI. | [optional] [readonly] 
**uuid** | **str** | Schedule Identifier. | [optional] [readonly] 
**type** | [**CrossConnectScheduleResponseType**](CrossConnectScheduleResponseType.md) |  | [optional] 
**code** | [**ScheduleType**](ScheduleType.md) |  | [optional] [readonly] 
**state** | [**CrossConnectScheduleState**](CrossConnectScheduleState.md) |  | [optional] [readonly] 
**auto_convert_to_standard** | **bool** | Indicates whether the Cross Connect is scheduled as STANDARD when no EXPEDITE scheduling is available. Returned only for EXPEDITE schedule.  | [optional] [readonly] 
**readiness_date_time** | **datetime** | Carrier Circuit delivery date is the date when the Carrier commits to enable the circuit. Your order will be placed on hold, pending the date you enter. Equinix will wait for the Carrier to deliver the service and then will complete the installation.  | [optional] [readonly] 
**requested_date_time** | **datetime** | Requested Installation Date and Time. | [optional] [readonly] 
**equinix_proposed_date_time** | **datetime** | Date and Time proposed by Equinix when the EXPEDITE schedule is not available.  | [optional] [readonly] 
**installation_date_time** | **datetime** | Installation Date and Time. | [optional] [readonly] 
**deinstallation_date_time** | **datetime** | Deinstallation Date and Time. Returned for a removal schedule. | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_schedule_response import CrossConnectScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectScheduleResponse from a JSON string
cross_connect_schedule_response_instance = CrossConnectScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectScheduleResponse.to_json())

# convert the object into a dict
cross_connect_schedule_response_dict = cross_connect_schedule_response_instance.to_dict()
# create an instance of CrossConnectScheduleResponse from a dict
cross_connect_schedule_response_from_dict = CrossConnectScheduleResponse.from_dict(cross_connect_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


