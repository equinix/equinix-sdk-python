# RouteFilterRulesPatchRequestItem

Route Filter Rule change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path to change | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_patch_request_item import RouteFilterRulesPatchRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesPatchRequestItem from a JSON string
route_filter_rules_patch_request_item_instance = RouteFilterRulesPatchRequestItem.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesPatchRequestItem.to_json())

# convert the object into a dict
route_filter_rules_patch_request_item_dict = route_filter_rules_patch_request_item_instance.to_dict()
# create an instance of RouteFilterRulesPatchRequestItem from a dict
route_filter_rules_patch_request_item_from_dict = RouteFilterRulesPatchRequestItem.from_dict(route_filter_rules_patch_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


