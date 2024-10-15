# CloudRouterActionsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CloudRouterActionResponse]**](CloudRouterActionResponse.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_response import CloudRouterActionsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchResponse from a JSON string
cloud_router_actions_search_response_instance = CloudRouterActionsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchResponse.to_json())

# convert the object into a dict
cloud_router_actions_search_response_dict = cloud_router_actions_search_response_instance.to_dict()
# create an instance of CloudRouterActionsSearchResponse from a dict
cloud_router_actions_search_response_form_dict = cloud_router_actions_search_response.from_dict(cloud_router_actions_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


