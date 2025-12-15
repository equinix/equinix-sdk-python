# StreamSubscriptionPostRequest

Create Stream Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**StreamSubscriptionPostRequestType**](StreamSubscriptionPostRequestType.md) |  | 
**name** | **str** | Customer-provided stream subscription name | 
**description** | **str** | Customer-provided stream subscription description | [optional] 
**enabled** | **bool** | Stream subscription enabled status | [optional] [default to True]
**metric_selector** | [**StreamSubscriptionSelector**](StreamSubscriptionSelector.md) |  | [optional] 
**event_selector** | [**StreamSubscriptionSelector**](StreamSubscriptionSelector.md) |  | [optional] 
**sink** | [**StreamSubscriptionSink**](StreamSubscriptionSink.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_post_request import StreamSubscriptionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionPostRequest from a JSON string
stream_subscription_post_request_instance = StreamSubscriptionPostRequest.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionPostRequest.to_json())

# convert the object into a dict
stream_subscription_post_request_dict = stream_subscription_post_request_instance.to_dict()
# create an instance of StreamSubscriptionPostRequest from a dict
stream_subscription_post_request_from_dict = StreamSubscriptionPostRequest.from_dict(stream_subscription_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


