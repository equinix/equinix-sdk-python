# RouteFilterRuleAndExpression

AND expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteFilterRuleExpression]**](RouteFilterRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rule_and_expression import RouteFilterRuleAndExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRuleAndExpression from a JSON string
route_filter_rule_and_expression_instance = RouteFilterRuleAndExpression.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRuleAndExpression.to_json())

# convert the object into a dict
route_filter_rule_and_expression_dict = route_filter_rule_and_expression_instance.to_dict()
# create an instance of RouteFilterRuleAndExpression from a dict
route_filter_rule_and_expression_from_dict = RouteFilterRuleAndExpression.from_dict(route_filter_rule_and_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


