# RouteFilterRuleSimpleExpression

Simple filter expression with property, operator, and values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:  * &#x60;/type&#x60; - Route Filter Rules Type  * &#x60;/name&#x60; - Route Filter Rules Name  * &#x60;/uuid&#x60; - Route Filter Rules uuid  * &#x60;/state&#x60; - Route Filter Rules status  * &#x60;/prefix&#x60; - Route Filter Rule Prefix  * &#x60;/prefixMatch&#x60; - Route Filter Rule Prefix Match  | [optional] 
**operator** | **str** | Possible operators to use on filters:  * &#x60;&#x3D;&#x60; - equal  * &#x60;!&#x3D;&#x60; - not equal  * &#x60;[NOT] LIKE&#x60; - (not) like  * &#x60;[NOT] IN&#x60; - (not) in  * &#x60;ILIKE&#x60; - case-insensitive like  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rule_simple_expression import RouteFilterRuleSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRuleSimpleExpression from a JSON string
route_filter_rule_simple_expression_instance = RouteFilterRuleSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRuleSimpleExpression.to_json())

# convert the object into a dict
route_filter_rule_simple_expression_dict = route_filter_rule_simple_expression_instance.to_dict()
# create an instance of RouteFilterRuleSimpleExpression from a dict
route_filter_rule_simple_expression_from_dict = RouteFilterRuleSimpleExpression.from_dict(route_filter_rule_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


