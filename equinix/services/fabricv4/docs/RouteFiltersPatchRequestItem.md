# RouteFiltersPatchRequestItem

Route Filter change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path to change | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.route_filters_patch_request_item import RouteFiltersPatchRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersPatchRequestItem from a JSON string
route_filters_patch_request_item_instance = RouteFiltersPatchRequestItem.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersPatchRequestItem.to_json())

# convert the object into a dict
route_filters_patch_request_item_dict = route_filters_patch_request_item_instance.to_dict()
# create an instance of RouteFiltersPatchRequestItem from a dict
route_filters_patch_request_item_form_dict = route_filters_patch_request_item.from_dict(route_filters_patch_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


