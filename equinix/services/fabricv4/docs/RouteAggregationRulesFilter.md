# RouteAggregationRulesFilter

Top-level filter that can be either an AND expression or OR expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteAggregationRuleExpression]**](RouteAggregationRuleExpression.md) |  | [optional] 
**var_or** | [**List[RouteAggregationRuleExpression]**](RouteAggregationRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_filter import RouteAggregationRulesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesFilter from a JSON string
route_aggregation_rules_filter_instance = RouteAggregationRulesFilter.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesFilter.to_json())

# convert the object into a dict
route_aggregation_rules_filter_dict = route_aggregation_rules_filter_instance.to_dict()
# create an instance of RouteAggregationRulesFilter from a dict
route_aggregation_rules_filter_from_dict = RouteAggregationRulesFilter.from_dict(route_aggregation_rules_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


