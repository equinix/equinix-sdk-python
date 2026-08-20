# SearchStreamSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamSubscription]**](StreamSubscription.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_stream_subscription_response import SearchStreamSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStreamSubscriptionResponse from a JSON string
search_stream_subscription_response_instance = SearchStreamSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SearchStreamSubscriptionResponse.to_json())

# convert the object into a dict
search_stream_subscription_response_dict = search_stream_subscription_response_instance.to_dict()
# create an instance of SearchStreamSubscriptionResponse from a dict
search_stream_subscription_response_from_dict = SearchStreamSubscriptionResponse.from_dict(search_stream_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


