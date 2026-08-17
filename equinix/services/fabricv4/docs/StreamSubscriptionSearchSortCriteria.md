# StreamSubscriptionSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**StreamSubscriptionSearchSortDirection**](StreamSubscriptionSearchSortDirection.md) |  | [default to StreamSubscriptionSearchSortDirection.DESC]
**var_property** | [**StreamSubscriptionSearchSortBy**](StreamSubscriptionSearchSortBy.md) |  | [default to StreamSubscriptionSearchSortBy.CREATEDDATETIME]

## Example

```python
from equinix.services.fabricv4.models.stream_subscription_search_sort_criteria import StreamSubscriptionSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSubscriptionSearchSortCriteria from a JSON string
stream_subscription_search_sort_criteria_instance = StreamSubscriptionSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(StreamSubscriptionSearchSortCriteria.to_json())

# convert the object into a dict
stream_subscription_search_sort_criteria_dict = stream_subscription_search_sort_criteria_instance.to_dict()
# create an instance of StreamSubscriptionSearchSortCriteria from a dict
stream_subscription_search_sort_criteria_from_dict = StreamSubscriptionSearchSortCriteria.from_dict(stream_subscription_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


