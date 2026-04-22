# RouteAggregationRuleSimpleExpression

Simple filter expression with property, operator, and values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/type&#x60; - Route Aggregation Rules Type  * &#x60;/name&#x60; - Route Aggregation Rules Name  * &#x60;/uuid&#x60; - Route Aggregation Rules uuid  * &#x60;/state&#x60; - Route Aggregation Rules status  * &#x60;/prefix&#x60; - Route Aggregation Rule Prefix  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rule_simple_expression import RouteAggregationRuleSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRuleSimpleExpression from a JSON string
route_aggregation_rule_simple_expression_instance = RouteAggregationRuleSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRuleSimpleExpression.to_json())

# convert the object into a dict
route_aggregation_rule_simple_expression_dict = route_aggregation_rule_simple_expression_instance.to_dict()
# create an instance of RouteAggregationRuleSimpleExpression from a dict
route_aggregation_rule_simple_expression_from_dict = RouteAggregationRuleSimpleExpression.from_dict(route_aggregation_rule_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


