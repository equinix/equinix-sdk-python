# CrossConnectActionSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**CrossConnectSortCriteriaDirection**](CrossConnectSortCriteriaDirection.md) |  | [optional] [default to CrossConnectSortCriteriaDirection.DESC]
**var_property** | [**CrossConnectActionSortCriteriaProperty**](CrossConnectActionSortCriteriaProperty.md) |  | [optional] [default to CrossConnectActionSortCriteriaProperty.SLASH_CHANGE_LOG_SLASH_CREATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_sort_criteria import CrossConnectActionSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionSortCriteria from a JSON string
cross_connect_action_sort_criteria_instance = CrossConnectActionSortCriteria.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionSortCriteria.to_json())

# convert the object into a dict
cross_connect_action_sort_criteria_dict = cross_connect_action_sort_criteria_instance.to_dict()
# create an instance of CrossConnectActionSortCriteria from a dict
cross_connect_action_sort_criteria_from_dict = CrossConnectActionSortCriteria.from_dict(cross_connect_action_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


