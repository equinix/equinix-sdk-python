# RouteFilterRuleSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**RouteFilterRuleSortDirection**](RouteFilterRuleSortDirection.md) |  | [optional] [default to RouteFilterRuleSortDirection.DESC]
**var_property** | [**RouteFilterRuleSortBy**](RouteFilterRuleSortBy.md) |  | [optional] [default to RouteFilterRuleSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.route_filter_rule_sort_criteria import RouteFilterRuleSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRuleSortCriteria from a JSON string
route_filter_rule_sort_criteria_instance = RouteFilterRuleSortCriteria.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRuleSortCriteria.to_json())

# convert the object into a dict
route_filter_rule_sort_criteria_dict = route_filter_rule_sort_criteria_instance.to_dict()
# create an instance of RouteFilterRuleSortCriteria from a dict
route_filter_rule_sort_criteria_from_dict = RouteFilterRuleSortCriteria.from_dict(route_filter_rule_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


