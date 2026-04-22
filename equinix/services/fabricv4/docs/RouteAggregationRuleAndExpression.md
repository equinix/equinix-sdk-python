# RouteAggregationRuleAndExpression

AND expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteAggregationRuleExpression]**](RouteAggregationRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rule_and_expression import RouteAggregationRuleAndExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRuleAndExpression from a JSON string
route_aggregation_rule_and_expression_instance = RouteAggregationRuleAndExpression.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRuleAndExpression.to_json())

# convert the object into a dict
route_aggregation_rule_and_expression_dict = route_aggregation_rule_and_expression_instance.to_dict()
# create an instance of RouteAggregationRuleAndExpression from a dict
route_aggregation_rule_and_expression_from_dict = RouteAggregationRuleAndExpression.from_dict(route_aggregation_rule_and_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


