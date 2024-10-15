# GetSubscriptionsInStreamResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamGetSubscriptions]**](StreamGetSubscriptions.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_subscriptions_in_stream_response import GetSubscriptionsInStreamResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionsInStreamResponse from a JSON string
get_subscriptions_in_stream_response_instance = GetSubscriptionsInStreamResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionsInStreamResponse.to_json())

# convert the object into a dict
get_subscriptions_in_stream_response_dict = get_subscriptions_in_stream_response_instance.to_dict()
# create an instance of GetSubscriptionsInStreamResponse from a dict
get_subscriptions_in_stream_response_form_dict = get_subscriptions_in_stream_response.from_dict(get_subscriptions_in_stream_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


