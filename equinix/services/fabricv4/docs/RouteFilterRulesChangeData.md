# RouteFilterRulesChangeData

Current state of latest Route Filter Rules change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current outcome of the change flow | [optional] 
**created_by** | **str** | Created by User Key | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**data** | [**RouteFilterRulesChangeOperation**](RouteFilterRulesChangeOperation.md) |  | [optional] 
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteFilterRulesChangeType**](RouteFilterRulesChangeType.md) |  | 
**href** | **str** | Route Filter Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_change_data import RouteFilterRulesChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesChangeData from a JSON string
route_filter_rules_change_data_instance = RouteFilterRulesChangeData.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesChangeData.to_json())

# convert the object into a dict
route_filter_rules_change_data_dict = route_filter_rules_change_data_instance.to_dict()
# create an instance of RouteFilterRulesChangeData from a dict
route_filter_rules_change_data_from_dict = RouteFilterRulesChangeData.from_dict(route_filter_rules_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


