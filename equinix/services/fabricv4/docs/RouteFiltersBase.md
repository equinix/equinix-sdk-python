# RouteFiltersBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RouteFiltersBaseType**](RouteFiltersBaseType.md) |  | 
**name** | **str** |  | 
**description** | **str** | Customer-provided connection description | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.route_filters_base import RouteFiltersBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersBase from a JSON string
route_filters_base_instance = RouteFiltersBase.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersBase.to_json())

# convert the object into a dict
route_filters_base_dict = route_filters_base_instance.to_dict()
# create an instance of RouteFiltersBase from a dict
route_filters_base_from_dict = RouteFiltersBase.from_dict(route_filters_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


