# TimeServiceSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TimeServiceSortDirection**](TimeServiceSortDirection.md) |  | [optional] 
**var_property** | [**TimeServiceSortBy**](TimeServiceSortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_sort_criteria import TimeServiceSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServiceSortCriteria from a JSON string
time_service_sort_criteria_instance = TimeServiceSortCriteria.from_json(json)
# print the JSON string representation of the object
print(TimeServiceSortCriteria.to_json())

# convert the object into a dict
time_service_sort_criteria_dict = time_service_sort_criteria_instance.to_dict()
# create an instance of TimeServiceSortCriteria from a dict
time_service_sort_criteria_form_dict = time_service_sort_criteria.from_dict(time_service_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


