# RouteFiltersChange

Current state of latest Route Filter change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteFiltersChangeType**](RouteFiltersChangeType.md) |  | 
**href** | **str** | Route Filter Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_change import RouteFiltersChange

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersChange from a JSON string
route_filters_change_instance = RouteFiltersChange.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersChange.to_json())

# convert the object into a dict
route_filters_change_dict = route_filters_change_instance.to_dict()
# create an instance of RouteFiltersChange from a dict
route_filters_change_from_dict = RouteFiltersChange.from_dict(route_filters_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


