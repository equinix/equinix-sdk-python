# CloudRouterPostRequest

Create Cloud Router

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterPostRequestType**](CloudRouterPostRequestType.md) |  | 
**name** | **str** | Customer-provided Cloud Router name | 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 

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
cloud_router_post_request_from_dict = CloudRouterPostRequest.from_dict(cloud_router_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


