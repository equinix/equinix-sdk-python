# RouteAggregationRuleOrExpression

OR expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[RouteAggregationRuleExpression]**](RouteAggregationRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rule_or_expression import RouteAggregationRuleOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRuleOrExpression from a JSON string
route_aggregation_rule_or_expression_instance = RouteAggregationRuleOrExpression.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRuleOrExpression.to_json())

# convert the object into a dict
route_aggregation_rule_or_expression_dict = route_aggregation_rule_or_expression_instance.to_dict()
# create an instance of RouteAggregationRuleOrExpression from a dict
route_aggregation_rule_or_expression_from_dict = RouteAggregationRuleOrExpression.from_dict(route_aggregation_rule_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


