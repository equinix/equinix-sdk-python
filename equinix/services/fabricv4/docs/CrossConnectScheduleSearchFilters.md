# CrossConnectScheduleSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CrossConnectScheduleSearchSimpleExpressions]**](CrossConnectScheduleSearchSimpleExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_schedule_search_filters import CrossConnectScheduleSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectScheduleSearchFilters from a JSON string
cross_connect_schedule_search_filters_instance = CrossConnectScheduleSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CrossConnectScheduleSearchFilters.to_json())

# convert the object into a dict
cross_connect_schedule_search_filters_dict = cross_connect_schedule_search_filters_instance.to_dict()
# create an instance of CrossConnectScheduleSearchFilters from a dict
cross_connect_schedule_search_filters_from_dict = CrossConnectScheduleSearchFilters.from_dict(cross_connect_schedule_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


