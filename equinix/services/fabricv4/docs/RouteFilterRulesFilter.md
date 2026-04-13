# RouteFilterRulesFilter

Top-level filter that can be either an AND expression or OR expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[RouteFilterRuleExpression]**](RouteFilterRuleExpression.md) |  | [optional] 
**var_or** | [**List[RouteFilterRuleExpression]**](RouteFilterRuleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_filter import RouteFilterRulesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesFilter from a JSON string
route_filter_rules_filter_instance = RouteFilterRulesFilter.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesFilter.to_json())

# convert the object into a dict
route_filter_rules_filter_dict = route_filter_rules_filter_instance.to_dict()
# create an instance of RouteFilterRulesFilter from a dict
route_filter_rules_filter_from_dict = RouteFilterRulesFilter.from_dict(route_filter_rules_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


