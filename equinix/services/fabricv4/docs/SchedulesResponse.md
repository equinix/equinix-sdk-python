# SchedulesResponse

Schedules of the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CrossConnectScheduleResponse]**](CrossConnectScheduleResponse.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.schedules_response import SchedulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesResponse from a JSON string
schedules_response_instance = SchedulesResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulesResponse.to_json())

# convert the object into a dict
schedules_response_dict = schedules_response_instance.to_dict()
# create an instance of SchedulesResponse from a dict
schedules_response_from_dict = SchedulesResponse.from_dict(schedules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


