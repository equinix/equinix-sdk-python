# SearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**Expression**](Expression.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[SortCriteria]**](SortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print(SearchRequest.to_json())

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_from_dict = SearchRequest.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


