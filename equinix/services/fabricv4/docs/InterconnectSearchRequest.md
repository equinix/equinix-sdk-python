# InterconnectSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**InterconnectFilter**](InterconnectFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[InterconnectSortCriteria]**](InterconnectSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_search_request import InterconnectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectSearchRequest from a JSON string
interconnect_search_request_instance = InterconnectSearchRequest.from_json(json)
# print the JSON string representation of the object
print(InterconnectSearchRequest.to_json())

# convert the object into a dict
interconnect_search_request_dict = interconnect_search_request_instance.to_dict()
# create an instance of InterconnectSearchRequest from a dict
interconnect_search_request_from_dict = InterconnectSearchRequest.from_dict(interconnect_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


