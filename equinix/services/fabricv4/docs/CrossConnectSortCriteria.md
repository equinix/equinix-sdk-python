# CrossConnectSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**CrossConnectSortCriteriaDirection**](CrossConnectSortCriteriaDirection.md) |  | [optional] [default to CrossConnectSortCriteriaDirection.DESC]
**var_property** | [**CrossConnectSortCriteriaProperty**](CrossConnectSortCriteriaProperty.md) |  | [optional] [default to CrossConnectSortCriteriaProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.cross_connect_sort_criteria import CrossConnectSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectSortCriteria from a JSON string
cross_connect_sort_criteria_instance = CrossConnectSortCriteria.from_json(json)
# print the JSON string representation of the object
print(CrossConnectSortCriteria.to_json())

# convert the object into a dict
cross_connect_sort_criteria_dict = cross_connect_sort_criteria_instance.to_dict()
# create an instance of CrossConnectSortCriteria from a dict
cross_connect_sort_criteria_from_dict = CrossConnectSortCriteria.from_dict(cross_connect_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


