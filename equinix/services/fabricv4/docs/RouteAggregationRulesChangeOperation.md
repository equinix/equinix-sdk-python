# RouteAggregationRulesChangeOperation

Route Aggregation Rule change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**RoutingProtocolChangeOperationOp**](RoutingProtocolChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | [**RouteAggregationRulesBase**](RouteAggregationRulesBase.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_change_operation import RouteAggregationRulesChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesChangeOperation from a JSON string
route_aggregation_rules_change_operation_instance = RouteAggregationRulesChangeOperation.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesChangeOperation.to_json())

# convert the object into a dict
route_aggregation_rules_change_operation_dict = route_aggregation_rules_change_operation_instance.to_dict()
# create an instance of RouteAggregationRulesChangeOperation from a dict
route_aggregation_rules_change_operation_form_dict = route_aggregation_rules_change_operation.from_dict(route_aggregation_rules_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


