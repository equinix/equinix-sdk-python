# RouteFilterRuleOrExpression

OR expression containing multiple filter expressions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[RouteFilterRuleExpression]**](RouteFilterRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rule_or_expression import RouteFilterRuleOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRuleOrExpression from a JSON string
route_filter_rule_or_expression_instance = RouteFilterRuleOrExpression.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRuleOrExpression.to_json())

# convert the object into a dict
route_filter_rule_or_expression_dict = route_filter_rule_or_expression_instance.to_dict()
# create an instance of RouteFilterRuleOrExpression from a dict
route_filter_rule_or_expression_from_dict = RouteFilterRuleOrExpression.from_dict(route_filter_rule_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


