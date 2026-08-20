# StreamSubscriptionSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[StreamSubscriptionSearchFilter]**](StreamSubscriptionSearchFilter.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_search_filters import StreamSubscriptionSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSearchFilters from a JSON string
stream_subscription_search_filters_instance = StreamSubscriptionSearchFilters.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSearchFilters.to_json())

# convert the object into a dict
stream_subscription_search_filters_dict = stream_subscription_search_filters_instance.to_dict()
# create an instance of StreamSubscriptionSearchFilters from a dict
stream_subscription_search_filters_from_dict = StreamSubscriptionSearchFilters.from_dict(stream_subscription_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


