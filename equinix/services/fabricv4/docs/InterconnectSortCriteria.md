# InterconnectSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**InterconnectSortDirection**](InterconnectSortDirection.md) |  | [optional] [default to InterconnectSortDirection.DESC]
**var_property** | [**InterconnectSortBy**](InterconnectSortBy.md) |  | [optional] [default to InterconnectSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.interconnect_sort_criteria import InterconnectSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectSortCriteria from a JSON string
interconnect_sort_criteria_instance = InterconnectSortCriteria.from_json(json)
# print the JSON string representation of the object
print(InterconnectSortCriteria.to_json())

# convert the object into a dict
interconnect_sort_criteria_dict = interconnect_sort_criteria_instance.to_dict()
# create an instance of InterconnectSortCriteria from a dict
interconnect_sort_criteria_from_dict = InterconnectSortCriteria.from_dict(interconnect_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


