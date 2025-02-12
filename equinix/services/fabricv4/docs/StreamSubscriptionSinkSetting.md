# StreamSubscriptionSinkSetting

Stream subscription sink settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_index** | **str** | event index | [optional] 
**metric_index** | **str** | metric index | [optional] 
**source** | **str** | source | [optional] 
**application_key** | **str** | Application key | [optional] 
**event_uri** | **str** | event uri | [optional] 
**metric_uri** | **str** | metric uri | [optional] 
**transform_alerts** | **bool** | transform alerts | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_sink_setting import StreamSubscriptionSinkSetting

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSinkSetting from a JSON string
stream_subscription_sink_setting_instance = StreamSubscriptionSinkSetting.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSinkSetting.to_json())

# convert the object into a dict
stream_subscription_sink_setting_dict = stream_subscription_sink_setting_instance.to_dict()
# create an instance of StreamSubscriptionSinkSetting from a dict
stream_subscription_sink_setting_from_dict = StreamSubscriptionSinkSetting.from_dict(stream_subscription_sink_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


