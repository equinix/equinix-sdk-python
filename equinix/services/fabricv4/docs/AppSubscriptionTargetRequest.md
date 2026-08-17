# AppSubscriptionTargetRequest

Target details for the Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_service** | [**AppSubscriptionTargetRequestAppService**](AppSubscriptionTargetRequestAppService.md) |  | [optional] 
**geo_scope** | **str** | Geo scope | 
**prioritization** | [**AppSubscriptionPrioritization**](AppSubscriptionPrioritization.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_target_request import AppSubscriptionTargetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionTargetRequest from a JSON string
app_subscription_target_request_instance = AppSubscriptionTargetRequest.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionTargetRequest.to_json())

# convert the object into a dict
app_subscription_target_request_dict = app_subscription_target_request_instance.to_dict()
# create an instance of AppSubscriptionTargetRequest from a dict
app_subscription_target_request_from_dict = AppSubscriptionTargetRequest.from_dict(app_subscription_target_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


