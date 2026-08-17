# AppSubscriptionSourceAppLink

App Link reference for App Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | **str** | App Link Type | [optional] 
**uuid** | **str** | Equinix-assigned access point identifier | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_source_app_link import AppSubscriptionSourceAppLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSourceAppLink from a JSON string
app_subscription_source_app_link_instance = AppSubscriptionSourceAppLink.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSourceAppLink.to_json())

# convert the object into a dict
app_subscription_source_app_link_dict = app_subscription_source_app_link_instance.to_dict()
# create an instance of AppSubscriptionSourceAppLink from a dict
app_subscription_source_app_link_from_dict = AppSubscriptionSourceAppLink.from_dict(app_subscription_source_app_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


