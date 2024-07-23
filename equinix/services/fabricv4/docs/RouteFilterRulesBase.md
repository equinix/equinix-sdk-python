# RouteFilterRulesBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided Route Filter Rule description | [optional] 
**prefix** | **str** |  | 
**prefix_match** | **str** |  | [optional] [default to 'orlonger']

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_base import RouteFilterRulesBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesBase from a JSON string
route_filter_rules_base_instance = RouteFilterRulesBase.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesBase.to_json())

# convert the object into a dict
route_filter_rules_base_dict = route_filter_rules_base_instance.to_dict()
# create an instance of RouteFilterRulesBase from a dict
route_filter_rules_base_form_dict = route_filter_rules_base.from_dict(route_filter_rules_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


