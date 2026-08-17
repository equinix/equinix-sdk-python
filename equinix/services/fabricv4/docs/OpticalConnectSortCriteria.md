# OpticalConnectSortCriteria

Sorting to apply to search results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**OpticalConnectSortDirection**](OpticalConnectSortDirection.md) |  | [optional] [default to OpticalConnectSortDirection.DESC]
**var_property** | [**OpticalConnectSortBy**](OpticalConnectSortBy.md) |  | [optional] [default to OpticalConnectSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.optical_connect_sort_criteria import OpticalConnectSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectSortCriteria from a JSON string
optical_connect_sort_criteria_instance = OpticalConnectSortCriteria.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectSortCriteria.to_json())

# convert the object into a dict
optical_connect_sort_criteria_dict = optical_connect_sort_criteria_instance.to_dict()
# create an instance of OpticalConnectSortCriteria from a dict
optical_connect_sort_criteria_from_dict = OpticalConnectSortCriteria.from_dict(optical_connect_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


