# CloudRouterSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudRouterFilters**](CloudRouterFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CloudRouterSortCriteria]**](CloudRouterSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_search_request import CloudRouterSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterSearchRequest from a JSON string
cloud_router_search_request_instance = CloudRouterSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterSearchRequest.to_json())

# convert the object into a dict
cloud_router_search_request_dict = cloud_router_search_request_instance.to_dict()
# create an instance of CloudRouterSearchRequest from a dict
cloud_router_search_request_form_dict = cloud_router_search_request.from_dict(cloud_router_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


