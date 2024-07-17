# GetAllConnectionRouteFiltersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionRouteFilterData]**](ConnectionRouteFilterData.md) | List of Route Filters attached to a Connection | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_connection_route_filters_response import GetAllConnectionRouteFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllConnectionRouteFiltersResponse from a JSON string
get_all_connection_route_filters_response_instance = GetAllConnectionRouteFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllConnectionRouteFiltersResponse.to_json())

# convert the object into a dict
get_all_connection_route_filters_response_dict = get_all_connection_route_filters_response_instance.to_dict()
# create an instance of GetAllConnectionRouteFiltersResponse from a dict
get_all_connection_route_filters_response_form_dict = get_all_connection_route_filters_response.from_dict(get_all_connection_route_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


