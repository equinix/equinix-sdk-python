# AppSubscription

App Subscription object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppSubscriptionType**](AppSubscriptionType.md) |  | [default to AppSubscriptionType.APP_SUBSCRIPTION]
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**source** | [**AppSubscriptionSource**](AppSubscriptionSource.md) |  | 
**target** | [**AppSubscriptionTarget**](AppSubscriptionTarget.md) |  | 
**state** | [**AppSubscriptionState**](AppSubscriptionState.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**AppSubscriptionChange**](AppSubscriptionChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_subscription import AppSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscription from a JSON string
app_subscription_instance = AppSubscription.from_json(json)
# print the JSON string representation of the object
print(AppSubscription.to_json())

# convert the object into a dict
app_subscription_dict = app_subscription_instance.to_dict()
# create an instance of AppSubscription from a dict
app_subscription_from_dict = AppSubscription.from_dict(app_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


