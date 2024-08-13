# SubscriptionResponse

Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**status** | [**SubscriptionStatus**](SubscriptionStatus.md) |  | [optional] 
**marketplace** | [**SubscriptionResponseMarketplace**](SubscriptionResponseMarketplace.md) |  | [optional] 
**offer_type** | [**SubscriptionResponseOfferType**](SubscriptionResponseOfferType.md) |  | [optional] 
**is_auto_renew** | **bool** |  | [optional] 
**offer_id** | **str** |  | [optional] 
**trial** | [**SubscriptionTrial**](SubscriptionTrial.md) |  | [optional] 
**subscription_key** | **str** |  | [optional] 
**entitlements** | [**List[SubscriptionEntitlementResponse]**](SubscriptionEntitlementResponse.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_form_dict = subscription_response.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


