# CrossConnectScheduleSearchRequest

Search Cross Connect schedules based on filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CrossConnectScheduleSearchFilters**](CrossConnectScheduleSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CrossConnectScheduleSortCriteria]**](CrossConnectScheduleSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_schedule_search_request import CrossConnectScheduleSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectScheduleSearchRequest from a JSON string
cross_connect_schedule_search_request_instance = CrossConnectScheduleSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectScheduleSearchRequest.to_json())

# convert the object into a dict
cross_connect_schedule_search_request_dict = cross_connect_schedule_search_request_instance.to_dict()
# create an instance of CrossConnectScheduleSearchRequest from a dict
cross_connect_schedule_search_request_from_dict = CrossConnectScheduleSearchRequest.from_dict(cross_connect_schedule_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


