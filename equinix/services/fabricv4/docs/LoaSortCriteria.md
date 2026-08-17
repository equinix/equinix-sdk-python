# LoaSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ExchangeServiceSearchSortCriteriaDirection**](ExchangeServiceSearchSortCriteriaDirection.md) |  | [optional] [default to ExchangeServiceSearchSortCriteriaDirection.DESC]
**var_property** | [**LoaSortCriteriaProperty**](LoaSortCriteriaProperty.md) |  | [optional] [default to LoaSortCriteriaProperty.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.loa_sort_criteria import LoaSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of LoaSortCriteria from a JSON string
loa_sort_criteria_instance = LoaSortCriteria.from_json(json)
# print the JSON string representation of the object
print(LoaSortCriteria.to_json())

# convert the object into a dict
loa_sort_criteria_dict = loa_sort_criteria_instance.to_dict()
# create an instance of LoaSortCriteria from a dict
loa_sort_criteria_from_dict = LoaSortCriteria.from_dict(loa_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


