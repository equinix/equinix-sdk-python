# SearchSchedulesResponse

List of Cross Connect schedule windows offered at an IBX.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[CrossConnectScheduleSortCriteria]**](CrossConnectScheduleSortCriteria.md) |  | [optional] 
**data** | [**List[CrossConnectScheduleAvailability]**](CrossConnectScheduleAvailability.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.search_schedules_response import SearchSchedulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSchedulesResponse from a JSON string
search_schedules_response_instance = SearchSchedulesResponse.from_json(json)
# print the JSON string representation of the object
print(SearchSchedulesResponse.to_json())

# convert the object into a dict
search_schedules_response_dict = search_schedules_response_instance.to_dict()
# create an instance of SearchSchedulesResponse from a dict
search_schedules_response_from_dict = SearchSchedulesResponse.from_dict(search_schedules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


