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
**bgp_ipv4_routes_count** | **int** | Access point used and maximum number of IPv4 BGP routes | [optional] 
**bgp_ipv6_routes_count** | **int** | Access point used and maximum number of IPv6 BGP routes | [optional] 
**connections_count** | **int** | Number of connections associated with this Access point | [optional] 
**distinct_ipv4_prefixes_count** | **int** | Number of distinct ipv4 routes | [optional] 
**distinct_ipv6_prefixes_count** | **int** | Number of distinct ipv6 routes | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**CloudRouterChange**](CloudRouterChange.md) |  | [optional] 
**type** | [**CloudRouterPostRequestType**](CloudRouterPostRequestType.md) |  | [optional] 
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
cloud_router_form_dict = cloud_router.from_dict(cloud_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


