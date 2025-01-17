# StreamGetSubscriptions

Stream object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream Get Stream Subscriptions URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**type** | [**StreamGetSubscriptionsType**](StreamGetSubscriptionsType.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_get_subscriptions import StreamGetSubscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of StreamGetSubscriptions from a JSON string
stream_get_subscriptions_instance = StreamGetSubscriptions.from_json(json)
# print the JSON string representation of the object
print(StreamGetSubscriptions.to_json())

# convert the object into a dict
stream_get_subscriptions_dict = stream_get_subscriptions_instance.to_dict()
# create an instance of StreamGetSubscriptions from a dict
stream_get_subscriptions_from_dict = StreamGetSubscriptions.from_dict(stream_get_subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


