# AppSubscriptionSource

Source details for the Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_link** | [**AppSubscriptionSourceAppLink**](AppSubscriptionSourceAppLink.md) |  | [optional] 
**ip_subnets** | **List[str]** | List of IP subnets in CIDR notation | 

## Example

```python
from equinix.services.fabricv4.models.app_subscription_source import AppSubscriptionSource

# TODO update the JSON string below
json = "{}"
# create an instance of AppSubscriptionSource from a JSON string
app_subscription_source_instance = AppSubscriptionSource.from_json(json)
# print the JSON string representation of the object
print(AppSubscriptionSource.to_json())

# convert the object into a dict
app_subscription_source_dict = app_subscription_source_instance.to_dict()
# create an instance of AppSubscriptionSource from a dict
app_subscription_source_from_dict = AppSubscriptionSource.from_dict(app_subscription_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


