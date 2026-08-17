# StreamSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**StreamSearchSortDirection**](StreamSearchSortDirection.md) |  | [default to StreamSearchSortDirection.DESC]
**var_property** | [**StreamSearchSortBy**](StreamSearchSortBy.md) |  | [default to StreamSearchSortBy.CREATEDDATETIME]

## Example

```python
from equinix.services.fabricv4.models.stream_search_sort_criteria import StreamSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSearchSortCriteria from a JSON string
stream_search_sort_criteria_instance = StreamSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(StreamSearchSortCriteria.to_json())

# convert the object into a dict
stream_search_sort_criteria_dict = stream_search_sort_criteria_instance.to_dict()
# create an instance of StreamSearchSortCriteria from a dict
stream_search_sort_criteria_from_dict = StreamSearchSortCriteria.from_dict(stream_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


