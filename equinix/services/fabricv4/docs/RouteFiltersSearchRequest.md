# RouteFiltersSearchRequest

Search route filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**SearchFilter**](SearchFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[RouteFilterSortCriteria]**](RouteFilterSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_search_request import RouteFiltersSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersSearchRequest from a JSON string
route_filters_search_request_instance = RouteFiltersSearchRequest.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersSearchRequest.to_json())

# convert the object into a dict
route_filters_search_request_dict = route_filters_search_request_instance.to_dict()
# create an instance of RouteFiltersSearchRequest from a dict
route_filters_search_request_from_dict = RouteFiltersSearchRequest.from_dict(route_filters_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


