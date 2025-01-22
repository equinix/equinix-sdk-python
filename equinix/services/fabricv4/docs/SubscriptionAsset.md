# SubscriptionAsset

Asset information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the subscription asset ( XF_ROUTER ,IP_VC, IPWAN_VC ) | [optional] 
**package** | [**SubscriptionRouterPackageType**](SubscriptionRouterPackageType.md) |  | [optional] 
**bandwidth** | **int** | Bandwidth of the asset in Mbps | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subscription_asset import SubscriptionAsset

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAsset from a JSON string
subscription_asset_instance = SubscriptionAsset.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAsset.to_json())

# convert the object into a dict
subscription_asset_dict = subscription_asset_instance.to_dict()
# create an instance of SubscriptionAsset from a dict
subscription_asset_from_dict = SubscriptionAsset.from_dict(subscription_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


