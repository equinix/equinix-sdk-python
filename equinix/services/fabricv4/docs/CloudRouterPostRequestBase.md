# CloudRouterPostRequestBase

Create Cloud Router

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterPostRequestBaseType**](CloudRouterPostRequestBaseType.md) |  | [optional] 
**name** | **str** | Customer-provided Cloud Router name | [optional] 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_post_request_base import CloudRouterPostRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterPostRequestBase from a JSON string
cloud_router_post_request_base_instance = CloudRouterPostRequestBase.from_json(json)
# print the JSON string representation of the object
print(CloudRouterPostRequestBase.to_json())

# convert the object into a dict
cloud_router_post_request_base_dict = cloud_router_post_request_base_instance.to_dict()
# create an instance of CloudRouterPostRequestBase from a dict
cloud_router_post_request_base_from_dict = CloudRouterPostRequestBase.from_dict(cloud_router_post_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


