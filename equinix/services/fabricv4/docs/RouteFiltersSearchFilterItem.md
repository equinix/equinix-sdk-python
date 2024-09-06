# RouteFiltersSearchFilterItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**RouteFiltersSearchFilterItemProperty**](RouteFiltersSearchFilterItemProperty.md) |  | [optional] 
**operator** | **str** |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_search_filter_item import RouteFiltersSearchFilterItem

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersSearchFilterItem from a JSON string
route_filters_search_filter_item_instance = RouteFiltersSearchFilterItem.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersSearchFilterItem.to_json())

# convert the object into a dict
route_filters_search_filter_item_dict = route_filters_search_filter_item_instance.to_dict()
# create an instance of RouteFiltersSearchFilterItem from a dict
route_filters_search_filter_item_from_dict = RouteFiltersSearchFilterItem.from_dict(route_filters_search_filter_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


