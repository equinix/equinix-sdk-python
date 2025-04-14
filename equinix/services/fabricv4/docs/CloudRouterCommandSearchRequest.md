# CloudRouterCommandSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudRouterCommandSearchFilters**](CloudRouterCommandSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CloudRouterCommandSearchSortCriteria]**](CloudRouterCommandSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_search_request import CloudRouterCommandSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandSearchRequest from a JSON string
cloud_router_command_search_request_instance = CloudRouterCommandSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandSearchRequest.to_json())

# convert the object into a dict
cloud_router_command_search_request_dict = cloud_router_command_search_request_instance.to_dict()
# create an instance of CloudRouterCommandSearchRequest from a dict
cloud_router_command_search_request_from_dict = CloudRouterCommandSearchRequest.from_dict(cloud_router_command_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


