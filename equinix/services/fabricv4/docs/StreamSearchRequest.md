# StreamSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**StreamSearchFilters**](StreamSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[StreamSearchSortCriteria]**](StreamSearchSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_search_request import StreamSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSearchRequest from a JSON string
stream_search_request_instance = StreamSearchRequest.from_json(json)
# print the JSON string representation of the object
print(StreamSearchRequest.to_json())

# convert the object into a dict
stream_search_request_dict = stream_search_request_instance.to_dict()
# create an instance of StreamSearchRequest from a dict
stream_search_request_from_dict = StreamSearchRequest.from_dict(stream_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


