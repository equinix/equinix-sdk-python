# StreamSubscription

Stream Subscription object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream Subscription URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**type** | [**StreamSubscriptionType**](StreamSubscriptionType.md) |  | [optional] 
**name** | **str** | Customer-provided subscription name | [optional] 
**description** | **str** | Customer-provided subscription description | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**state** | [**StreamSubscriptionState**](StreamSubscriptionState.md) |  | [optional] 
**enabled** | **bool** | Stream subscription enabled status | [optional] 
**stream** | [**StreamTarget**](StreamTarget.md) |  | [optional] 
**filters** | [**StreamSubscriptionFilter**](StreamSubscriptionFilter.md) |  | [optional] 
**sink** | [**StreamSubscriptionSink**](StreamSubscriptionSink.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription import StreamSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscription from a JSON string
stream_subscription_instance = StreamSubscription.from_json(json)
# print the JSON string representation of the object
print(StreamSubscription.to_json())

# convert the object into a dict
stream_subscription_dict = stream_subscription_instance.to_dict()
# create an instance of StreamSubscription from a dict
stream_subscription_form_dict = stream_subscription.from_dict(stream_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

