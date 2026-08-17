# AppSubscriptionTargetRequestAppService

App Service reference for App Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Equinix-assigned access point identifier | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_target_request_app_service import AppSubscriptionTargetRequestAppService

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionTargetRequestAppService from a JSON string
app_subscription_target_request_app_service_instance = AppSubscriptionTargetRequestAppService.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionTargetRequestAppService.to_json())

# convert the object into a dict
app_subscription_target_request_app_service_dict = app_subscription_target_request_app_service_instance.to_dict()
# create an instance of AppSubscriptionTargetRequestAppService from a dict
app_subscription_target_request_app_service_from_dict = AppSubscriptionTargetRequestAppService.from_dict(app_subscription_target_request_app_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


