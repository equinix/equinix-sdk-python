# GetRouteFilterGetConnectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFilterConnectionsData]**](RouteFilterConnectionsData.md) | List of Connections using a Route Filter | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_route_filter_get_connections_response import GetRouteFilterGetConnectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteFilterGetConnectionsResponse from a JSON string
get_route_filter_get_connections_response_instance = GetRouteFilterGetConnectionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetRouteFilterGetConnectionsResponse.to_json())

# convert the object into a dict
get_route_filter_get_connections_response_dict = get_route_filter_get_connections_response_instance.to_dict()
# create an instance of GetRouteFilterGetConnectionsResponse from a dict
get_route_filter_get_connections_response_form_dict = get_route_filter_get_connections_response.from_dict(get_route_filter_get_connections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


