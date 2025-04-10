# CloudRouterCommand

Get Fabric Cloud Router Command response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**CloudRouterCommandType**](CloudRouterCommandType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 
**name** | **str** | Customer-provided Cloud Router name | [optional] 
**description** | **str** |  | [optional] 
**state** | [**CloudRouterCommandState**](CloudRouterCommandState.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**request** | [**CloudRouterCommandRequest**](CloudRouterCommandRequest.md) |  | [optional] 
**response** | [**CloudRouterCommandResponse**](CloudRouterCommandResponse.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command import CloudRouterCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommand from a JSON string
cloud_router_command_instance = CloudRouterCommand.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommand.to_json())

# convert the object into a dict
cloud_router_command_dict = cloud_router_command_instance.to_dict()
# create an instance of CloudRouterCommand from a dict
cloud_router_command_from_dict = CloudRouterCommand.from_dict(cloud_router_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


