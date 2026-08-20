# AppSubscriptionSourceRequest

Source details for the Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**AppSubscriptionSourceRequestAppLink**](AppSubscriptionSourceRequestAppLink.md) |  | [optional] 
**ip_subnets** | **List[str]** | List of IP subnets in CIDR notation | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_source_request import AppSubscriptionSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSourceRequest from a JSON string
app_subscription_source_request_instance = AppSubscriptionSourceRequest.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSourceRequest.to_json())

# convert the object into a dict
app_subscription_source_request_dict = app_subscription_source_request_instance.to_dict()
# create an instance of AppSubscriptionSourceRequest from a dict
app_subscription_source_request_from_dict = AppSubscriptionSourceRequest.from_dict(app_subscription_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


