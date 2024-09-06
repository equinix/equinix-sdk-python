# SubscriptionEntitlementResponse

Subscription entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Subscription Entitlement Id | [optional] 
**quantity_entitled** | **int** |  | [optional] 
**quantity_consumed** | **int** |  | [optional] 
**quantity_available** | **int** |  | [optional] 
**asset** | [**SubscriptionAsset**](SubscriptionAsset.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subscription_entitlement_response import SubscriptionEntitlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEntitlementResponse from a JSON string
subscription_entitlement_response_instance = SubscriptionEntitlementResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEntitlementResponse.to_json())

# convert the object into a dict
subscription_entitlement_response_dict = subscription_entitlement_response_instance.to_dict()
# create an instance of SubscriptionEntitlementResponse from a dict
subscription_entitlement_response_from_dict = SubscriptionEntitlementResponse.from_dict(subscription_entitlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


