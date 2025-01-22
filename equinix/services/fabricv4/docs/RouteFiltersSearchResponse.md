# RouteFiltersSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFiltersData]**](RouteFiltersData.md) | List of route filters | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_search_response import RouteFiltersSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersSearchResponse from a JSON string
route_filters_search_response_instance = RouteFiltersSearchResponse.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersSearchResponse.to_json())

# convert the object into a dict
route_filters_search_response_dict = route_filters_search_response_instance.to_dict()
# create an instance of RouteFiltersSearchResponse from a dict
route_filters_search_response_from_dict = RouteFiltersSearchResponse.from_dict(route_filters_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


