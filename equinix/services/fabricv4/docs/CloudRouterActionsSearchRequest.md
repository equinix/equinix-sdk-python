# CloudRouterActionsSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudRouterActionsSearchFilters**](CloudRouterActionsSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CloudRouterActionsSearchSortCriteria]**](CloudRouterActionsSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_request import CloudRouterActionsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchRequest from a JSON string
cloud_router_actions_search_request_instance = CloudRouterActionsSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchRequest.to_json())

# convert the object into a dict
cloud_router_actions_search_request_dict = cloud_router_actions_search_request_instance.to_dict()
# create an instance of CloudRouterActionsSearchRequest from a dict
cloud_router_actions_search_request_from_dict = CloudRouterActionsSearchRequest.from_dict(cloud_router_actions_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


