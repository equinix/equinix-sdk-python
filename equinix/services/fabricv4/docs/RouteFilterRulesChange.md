# RouteFilterRulesChange

Current state of latest route filter rule change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteFilterRulesChangeType**](RouteFilterRulesChangeType.md) |  | 
**href** | **str** | Route Filter Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_change import RouteFilterRulesChange

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesChange from a JSON string
route_filter_rules_change_instance = RouteFilterRulesChange.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesChange.to_json())

# convert the object into a dict
route_filter_rules_change_dict = route_filter_rules_change_instance.to_dict()
# create an instance of RouteFilterRulesChange from a dict
route_filter_rules_change_from_dict = RouteFilterRulesChange.from_dict(route_filter_rules_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


