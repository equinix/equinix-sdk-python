# RouteAggregationRuleSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**RouteAggregationRuleSortDirection**](RouteAggregationRuleSortDirection.md) |  | [optional] [default to RouteAggregationRuleSortDirection.DESC]
**var_property** | [**RouteAggregationRuleSortBy**](RouteAggregationRuleSortBy.md) |  | [optional] [default to RouteAggregationRuleSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rule_sort_criteria import RouteAggregationRuleSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRuleSortCriteria from a JSON string
route_aggregation_rule_sort_criteria_instance = RouteAggregationRuleSortCriteria.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRuleSortCriteria.to_json())

# convert the object into a dict
route_aggregation_rule_sort_criteria_dict = route_aggregation_rule_sort_criteria_instance.to_dict()
# create an instance of RouteAggregationRuleSortCriteria from a dict
route_aggregation_rule_sort_criteria_from_dict = RouteAggregationRuleSortCriteria.from_dict(route_aggregation_rule_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


