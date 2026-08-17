# StreamSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[StreamSearchFilter]**](StreamSearchFilter.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.stream_search_filters import StreamSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSearchFilters from a JSON string
stream_search_filters_instance = StreamSearchFilters.from_json(json)
# print the JSON string representation of the object
print(StreamSearchFilters.to_json())

# convert the object into a dict
stream_search_filters_dict = stream_search_filters_instance.to_dict()
# create an instance of StreamSearchFilters from a dict
stream_search_filters_from_dict = StreamSearchFilters.from_dict(stream_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


