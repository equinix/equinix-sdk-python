# StreamSubscriptionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[StreamFilter]**](StreamFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_filter import StreamSubscriptionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionFilter from a JSON string
stream_subscription_filter_instance = StreamSubscriptionFilter.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionFilter.to_json())

# convert the object into a dict
stream_subscription_filter_dict = stream_subscription_filter_instance.to_dict()
# create an instance of StreamSubscriptionFilter from a dict
stream_subscription_filter_from_dict = StreamSubscriptionFilter.from_dict(stream_subscription_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


