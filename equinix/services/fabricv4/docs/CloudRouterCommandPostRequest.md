# CloudRouterCommandPostRequest

Execute Cloud Router Command Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterCommandType**](CloudRouterCommandType.md) |  | 
**name** | **str** | Customer-provided Cloud Router Command name | [optional] 
**description** | **str** | Customer-provided Cloud Router Command description | [optional] 
**project** | [**Project**](Project.md) |  | 
**request** | [**CloudRouterCommandRequest**](CloudRouterCommandRequest.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_post_request import CloudRouterCommandPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandPostRequest from a JSON string
cloud_router_command_post_request_instance = CloudRouterCommandPostRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandPostRequest.to_json())

# convert the object into a dict
cloud_router_command_post_request_dict = cloud_router_command_post_request_instance.to_dict()
# create an instance of CloudRouterCommandPostRequest from a dict
cloud_router_command_post_request_from_dict = CloudRouterCommandPostRequest.from_dict(cloud_router_command_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


