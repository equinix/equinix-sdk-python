# AppSubscriptionPostRequest

Create App Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppSubscriptionType**](AppSubscriptionType.md) |  | [default to AppSubscriptionType.APP_SUBSCRIPTION]
**source** | [**AppSubscriptionSourceRequest**](AppSubscriptionSourceRequest.md) |  | [optional] 
**target** | [**AppSubscriptionTargetRequest**](AppSubscriptionTargetRequest.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_post_request import AppSubscriptionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionPostRequest from a JSON string
app_subscription_post_request_instance = AppSubscriptionPostRequest.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionPostRequest.to_json())

# convert the object into a dict
app_subscription_post_request_dict = app_subscription_post_request_instance.to_dict()
# create an instance of AppSubscriptionPostRequest from a dict
app_subscription_post_request_from_dict = AppSubscriptionPostRequest.from_dict(app_subscription_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


