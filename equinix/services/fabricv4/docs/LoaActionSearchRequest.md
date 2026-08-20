# LoaActionSearchRequest

Search loa actions based on filter criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**LoaActionSearchFilters**](LoaActionSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[LoaActionSortCriteria]**](LoaActionSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_search_request import LoaActionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionSearchRequest from a JSON string
loa_action_search_request_instance = LoaActionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(LoaActionSearchRequest.to_json())

# convert the object into a dict
loa_action_search_request_dict = loa_action_search_request_instance.to_dict()
# create an instance of LoaActionSearchRequest from a dict
loa_action_search_request_from_dict = LoaActionSearchRequest.from_dict(loa_action_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


