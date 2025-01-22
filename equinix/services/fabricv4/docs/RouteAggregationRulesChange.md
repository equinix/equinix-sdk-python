# RouteAggregationRulesChange

Current state of latest Route Aggregation Rule change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteAggregationRulesChangeType**](RouteAggregationRulesChangeType.md) |  | 
**href** | **str** | Route Aggregation Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_change import RouteAggregationRulesChange

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesChange from a JSON string
route_aggregation_rules_change_instance = RouteAggregationRulesChange.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesChange.to_json())

# convert the object into a dict
route_aggregation_rules_change_dict = route_aggregation_rules_change_instance.to_dict()
# create an instance of RouteAggregationRulesChange from a dict
route_aggregation_rules_change_from_dict = RouteAggregationRulesChange.from_dict(route_aggregation_rules_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


