# CloudRouterPostRequest

Create Cloud Router

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterPostRequestType**](CloudRouterPostRequestType.md) |  | [optional] 
**name** | **str** | Customer-provided Cloud Router name | [optional] 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_post_request import CloudRouterPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterPostRequest from a JSON string
cloud_router_post_request_instance = CloudRouterPostRequest.from_json(json)
# print the JSON string representation of the object
print(CloudRouterPostRequest.to_json())

# convert the object into a dict
cloud_router_post_request_dict = cloud_router_post_request_instance.to_dict()
# create an instance of CloudRouterPostRequest from a dict
cloud_router_post_request_form_dict = cloud_router_post_request.from_dict(cloud_router_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


