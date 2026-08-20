# LoaSearchRequest

Search loas based on filter criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**LoaSearchFilters**](LoaSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[LoaSortCriteria]**](LoaSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_search_request import LoaSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoaSearchRequest from a JSON string
loa_search_request_instance = LoaSearchRequest.from_json(json)
# print the JSON string representation of the object
print(LoaSearchRequest.to_json())

# convert the object into a dict
loa_search_request_dict = loa_search_request_instance.to_dict()
# create an instance of LoaSearchRequest from a dict
loa_search_request_from_dict = LoaSearchRequest.from_dict(loa_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


