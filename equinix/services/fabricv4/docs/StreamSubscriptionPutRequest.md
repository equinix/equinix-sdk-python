# StreamSubscriptionPutRequest

Update Stream Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer-provided stream subscription name | [optional] 
**description** | **str** | Customer-provided stream subscription description | [optional] 
**stream** | [**StreamTarget**](StreamTarget.md) |  | [optional] 
**enabled** | **bool** | Stream subscription enabled status | [optional] 
**filters** | [**StreamSubscriptionFilter**](StreamSubscriptionFilter.md) |  | [optional] 
**sink** | [**StreamSubscriptionSink**](StreamSubscriptionSink.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_put_request import StreamSubscriptionPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionPutRequest from a JSON string
stream_subscription_put_request_instance = StreamSubscriptionPutRequest.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionPutRequest.to_json())

# convert the object into a dict
stream_subscription_put_request_dict = stream_subscription_put_request_instance.to_dict()
# create an instance of StreamSubscriptionPutRequest from a dict
stream_subscription_put_request_form_dict = stream_subscription_put_request.from_dict(stream_subscription_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


