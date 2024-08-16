# SubscriptionAsset

Asset information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SubscriptionAssetType**](SubscriptionAssetType.md) |  | [optional] 
**package** | [**SubscriptionRouterPackageType**](SubscriptionRouterPackageType.md) |  | [optional] 
**bandwidth** | **int** |  | [optional] 

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
subscription_asset_form_dict = subscription_asset.from_dict(subscription_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

