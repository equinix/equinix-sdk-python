# StreamSubscriptionSink

Create Stream destination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** | any publicly reachable http endpoint | [optional] 
**type** | [**StreamSubscriptionSinkType**](StreamSubscriptionSinkType.md) |  | [optional] 
**batch_enabled** | **bool** | batch mode on/off | [optional] 
**batch_size_max** | **int** | maximum batch size | [optional] 
**batch_wait_time_max** | **int** | maximum batch waiting time | [optional] 
**credential** | [**StreamSubscriptionSinkCredential**](StreamSubscriptionSinkCredential.md) |  | [optional] 
**settings** | [**StreamSubscriptionSinkSetting**](StreamSubscriptionSinkSetting.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_sink import StreamSubscriptionSink

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSink from a JSON string
stream_subscription_sink_instance = StreamSubscriptionSink.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSink.to_json())

# convert the object into a dict
stream_subscription_sink_dict = stream_subscription_sink_instance.to_dict()
# create an instance of StreamSubscriptionSink from a dict
stream_subscription_sink_from_dict = StreamSubscriptionSink.from_dict(stream_subscription_sink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


