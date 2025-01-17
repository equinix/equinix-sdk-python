# RouteFilterRulesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Filter Rules URI | [optional] 
**type** | [**RouteFilterRulesDataType**](RouteFilterRulesDataType.md) |  | [optional] 
**uuid** | **str** | Route Filter Rule identifier | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided Route Filter Rule description | [optional] 
**state** | [**RouteFilterRuleState**](RouteFilterRuleState.md) |  | [optional] 
**prefix_match** | **str** | prefix matching operator | [optional] [default to 'orlonger']
**change** | [**RouteFilterRulesChange**](RouteFilterRulesChange.md) |  | [optional] 
**action** | [**RouteFilterRulesDataAction**](RouteFilterRulesDataAction.md) |  | [optional] 
**prefix** | **str** |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_data import RouteFilterRulesData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesData from a JSON string
route_filter_rules_data_instance = RouteFilterRulesData.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesData.to_json())

# convert the object into a dict
route_filter_rules_data_dict = route_filter_rules_data_instance.to_dict()
# create an instance of RouteFilterRulesData from a dict
route_filter_rules_data_from_dict = RouteFilterRulesData.from_dict(route_filter_rules_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


