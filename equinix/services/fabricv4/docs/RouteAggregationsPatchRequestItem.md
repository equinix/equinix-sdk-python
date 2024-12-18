# RouteAggregationsPatchRequestItem

Route Aggregation change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Handy shortcut for operation name | 
**path** | **str** | path to change | 
**value** | **object** | new value for updated parameter | 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_patch_request_item import RouteAggregationsPatchRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsPatchRequestItem from a JSON string
route_aggregations_patch_request_item_instance = RouteAggregationsPatchRequestItem.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsPatchRequestItem.to_json())

# convert the object into a dict
route_aggregations_patch_request_item_dict = route_aggregations_patch_request_item_instance.to_dict()
# create an instance of RouteAggregationsPatchRequestItem from a dict
route_aggregations_patch_request_item_form_dict = route_aggregations_patch_request_item.from_dict(route_aggregations_patch_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


