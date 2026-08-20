# StreamSubscriptionSearchOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[StreamSubscriptionSearchSimpleExpression]**](StreamSubscriptionSearchSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_search_or_filter import StreamSubscriptionSearchOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSearchOrFilter from a JSON string
stream_subscription_search_or_filter_instance = StreamSubscriptionSearchOrFilter.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSearchOrFilter.to_json())

# convert the object into a dict
stream_subscription_search_or_filter_dict = stream_subscription_search_or_filter_instance.to_dict()
# create an instance of StreamSubscriptionSearchOrFilter from a dict
stream_subscription_search_or_filter_from_dict = StreamSubscriptionSearchOrFilter.from_dict(stream_subscription_search_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


