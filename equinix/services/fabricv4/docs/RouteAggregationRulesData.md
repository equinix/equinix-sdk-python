# RouteAggregationRulesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Aggregation Rules URI | [optional] 
**type** | [**RouteAggregationRulesDataType**](RouteAggregationRulesDataType.md) |  | [optional] 
**uuid** | **str** | Route Aggregation Rule identifier | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided Route Aggregation Rule description | [optional] 
**state** | [**RouteAggregationRuleState**](RouteAggregationRuleState.md) |  | [optional] 
**change** | [**RouteAggregationRulesChange**](RouteAggregationRulesChange.md) |  | [optional] 
**prefix** | **str** |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_data import RouteAggregationRulesData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesData from a JSON string
route_aggregation_rules_data_instance = RouteAggregationRulesData.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesData.to_json())

# convert the object into a dict
route_aggregation_rules_data_dict = route_aggregation_rules_data_instance.to_dict()
# create an instance of RouteAggregationRulesData from a dict
route_aggregation_rules_data_form_dict = route_aggregation_rules_data.from_dict(route_aggregation_rules_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


