# RouteTableEntrySortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**RouteTableEntrySortDirection**](RouteTableEntrySortDirection.md) |  | [optional] [default to RouteTableEntrySortDirection.DESC]
**var_property** | [**RouteTableEntrySortBy**](RouteTableEntrySortBy.md) |  | [optional] [default to RouteTableEntrySortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.route_table_entry_sort_criteria import RouteTableEntrySortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTableEntrySortCriteria from a JSON string
route_table_entry_sort_criteria_instance = RouteTableEntrySortCriteria.from_json(json)
# print the JSON string representation of the object
print(RouteTableEntrySortCriteria.to_json())

# convert the object into a dict
route_table_entry_sort_criteria_dict = route_table_entry_sort_criteria_instance.to_dict()
# create an instance of RouteTableEntrySortCriteria from a dict
route_table_entry_sort_criteria_from_dict = RouteTableEntrySortCriteria.from_dict(route_table_entry_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


