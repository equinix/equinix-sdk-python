# ConnectionRouteSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ConnectionRouteEntryFilters**](ConnectionRouteEntryFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[ConnectionRouteSortCriteria]**](ConnectionRouteSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_route_search_request import ConnectionRouteSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteSearchRequest from a JSON string
connection_route_search_request_instance = ConnectionRouteSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteSearchRequest.to_json())

# convert the object into a dict
connection_route_search_request_dict = connection_route_search_request_instance.to_dict()
# create an instance of ConnectionRouteSearchRequest from a dict
connection_route_search_request_form_dict = connection_route_search_request.from_dict(connection_route_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


