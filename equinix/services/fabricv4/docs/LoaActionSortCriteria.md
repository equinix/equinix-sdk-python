# LoaActionSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ExchangeServiceSearchSortCriteriaDirection**](ExchangeServiceSearchSortCriteriaDirection.md) |  | [optional] [default to ExchangeServiceSearchSortCriteriaDirection.DESC]
**var_property** | [**LoaActionSortCriteriaProperty**](LoaActionSortCriteriaProperty.md) |  | [optional] [default to LoaActionSortCriteriaProperty.SLASH_CHANGE_LOG_SLASH_CREATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.loa_action_sort_criteria import LoaActionSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionSortCriteria from a JSON string
loa_action_sort_criteria_instance = LoaActionSortCriteria.from_json(json)
# print the JSON string representation of the object
print(LoaActionSortCriteria.to_json())

# convert the object into a dict
loa_action_sort_criteria_dict = loa_action_sort_criteria_instance.to_dict()
# create an instance of LoaActionSortCriteria from a dict
loa_action_sort_criteria_from_dict = LoaActionSortCriteria.from_dict(loa_action_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


