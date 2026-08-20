# AppServiceAttachedAppSubscription

App Subscription object attached to an App Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppSubscriptionType**](AppSubscriptionType.md) |  | [default to AppSubscriptionType.APP_SUBSCRIPTION]
**uuid** | **str** | Equinix-assigned access point identifier | 
**state** | [**AppSubscriptionState**](AppSubscriptionState.md) |  | 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_subscription import AppServiceAttachedAppSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppSubscription from a JSON string
app_service_attached_app_subscription_instance = AppServiceAttachedAppSubscription.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppSubscription.to_json())

# convert the object into a dict
app_service_attached_app_subscription_dict = app_service_attached_app_subscription_instance.to_dict()
# create an instance of AppServiceAttachedAppSubscription from a dict
app_service_attached_app_subscription_from_dict = AppServiceAttachedAppSubscription.from_dict(app_service_attached_app_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


