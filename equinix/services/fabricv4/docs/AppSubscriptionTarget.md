# AppSubscriptionTarget

Target details for the Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service** | [**AppSubscriptionTargetAppService**](AppSubscriptionTargetAppService.md) |  | [optional] 
**geo_scope** | **str** | Geo scope | 
**prioritization** | [**AppSubscriptionPrioritization**](AppSubscriptionPrioritization.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_target import AppSubscriptionTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionTarget from a JSON string
app_subscription_target_instance = AppSubscriptionTarget.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionTarget.to_json())

# convert the object into a dict
app_subscription_target_dict = app_subscription_target_instance.to_dict()
# create an instance of AppSubscriptionTarget from a dict
app_subscription_target_from_dict = AppSubscriptionTarget.from_dict(app_subscription_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


