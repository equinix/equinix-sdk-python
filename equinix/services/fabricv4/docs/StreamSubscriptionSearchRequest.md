# StreamSubscriptionSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**StreamSubscriptionSearchFilters**](StreamSubscriptionSearchFilters.md) |  | 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[StreamSubscriptionSearchSortCriteria]**](StreamSubscriptionSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_search_request import StreamSubscriptionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSearchRequest from a JSON string
stream_subscription_search_request_instance = StreamSubscriptionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSearchRequest.to_json())

# convert the object into a dict
stream_subscription_search_request_dict = stream_subscription_search_request_instance.to_dict()
# create an instance of StreamSubscriptionSearchRequest from a dict
stream_subscription_search_request_from_dict = StreamSubscriptionSearchRequest.from_dict(stream_subscription_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


