# CloudRouter

Fabric Cloud Router object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Cloud Routers URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**name** | **str** | Customer-provided Cloud Router name | [optional] 
**state** | [**CloudRouterAccessPointState**](CloudRouterAccessPointState.md) |  | [optional] 
**equinix_asn** | **int** | Equinix ASN | [optional] 
**connections_count** | **int** | Number of connections associated with this Access point | [optional] 
**gateway_attachments_count** | **int** | Number of gateway attachments associated with this Access point | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**CloudRouterChange**](CloudRouterChange.md) |  | [optional] 
**type** | [**CloudRouterPostRequestBaseType**](CloudRouterPostRequestBaseType.md) |  | [optional] 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router import CloudRouter

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouter from a JSON string
cloud_router_instance = CloudRouter.from_json(json)
# print the JSON string representation of the object
print(CloudRouter.to_json())

# convert the object into a dict
cloud_router_dict = cloud_router_instance.to_dict()
# create an instance of CloudRouter from a dict
cloud_router_from_dict = CloudRouter.from_dict(cloud_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


