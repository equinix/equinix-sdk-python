# CloudRouterCommandSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CloudRouterCommand]**](CloudRouterCommand.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_search_response import CloudRouterCommandSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandSearchResponse from a JSON string
cloud_router_command_search_response_instance = CloudRouterCommandSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandSearchResponse.to_json())

# convert the object into a dict
cloud_router_command_search_response_dict = cloud_router_command_search_response_instance.to_dict()
# create an instance of CloudRouterCommandSearchResponse from a dict
cloud_router_command_search_response_from_dict = CloudRouterCommandSearchResponse.from_dict(cloud_router_command_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


