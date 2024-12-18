# RouteAggregationRulesBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided Route Aggregation Rule description | [optional] 
**prefix** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_base import RouteAggregationRulesBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesBase from a JSON string
route_aggregation_rules_base_instance = RouteAggregationRulesBase.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesBase.to_json())

# convert the object into a dict
route_aggregation_rules_base_dict = route_aggregation_rules_base_instance.to_dict()
# create an instance of RouteAggregationRulesBase from a dict
route_aggregation_rules_base_form_dict = route_aggregation_rules_base.from_dict(route_aggregation_rules_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


