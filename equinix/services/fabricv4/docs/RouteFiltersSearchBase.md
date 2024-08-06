# RouteFiltersSearchBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**RouteFiltersSearchBaseFilter**](RouteFiltersSearchBaseFilter.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[SortItem]**](SortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_search_base import RouteFiltersSearchBase

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersSearchBase from a JSON string
route_filters_search_base_instance = RouteFiltersSearchBase.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersSearchBase.to_json())

# convert the object into a dict
route_filters_search_base_dict = route_filters_search_base_instance.to_dict()
# create an instance of RouteFiltersSearchBase from a dict
route_filters_search_base_from_dict = RouteFiltersSearchBase.from_dict(route_filters_search_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


