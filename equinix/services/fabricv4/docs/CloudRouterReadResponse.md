# CloudRouterReadResponse

Fabric Cloud Router read response object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**CloudRouterReadResponseType**](CloudRouterReadResponseType.md) |  | [optional] 
**name** | **str** | Customer-provided Cloud Router name | [optional] 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Preferences for notifications on connection configuration or status changes | [optional] 
**href** | **str** | Cloud Routers URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**state** | [**CloudRouterAccessPointState**](CloudRouterAccessPointState.md) |  | [optional] 
**equinix_asn** | **int** | Equinix ASN | [optional] 
**connections_count** | **int** | Number of connections associated with this Access point | [optional] 
**marketplace_subscription** | [**MarketplaceSubscription**](MarketplaceSubscription.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**CloudRouterChange**](CloudRouterChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_read_response import CloudRouterReadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterReadResponse from a JSON string
cloud_router_read_response_instance = CloudRouterReadResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterReadResponse.to_json())

# convert the object into a dict
cloud_router_read_response_dict = cloud_router_read_response_instance.to_dict()
# create an instance of CloudRouterReadResponse from a dict
cloud_router_read_response_from_dict = CloudRouterReadResponse.from_dict(cloud_router_read_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


