# CrossConnectActionSearchRequest

Search Cross Connect actions based on filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CrossConnectActionSearchFilters**](CrossConnectActionSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CrossConnectActionSortCriteria]**](CrossConnectActionSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_search_request import CrossConnectActionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionSearchRequest from a JSON string
cross_connect_action_search_request_instance = CrossConnectActionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionSearchRequest.to_json())

# convert the object into a dict
cross_connect_action_search_request_dict = cross_connect_action_search_request_instance.to_dict()
# create an instance of CrossConnectActionSearchRequest from a dict
cross_connect_action_search_request_from_dict = CrossConnectActionSearchRequest.from_dict(cross_connect_action_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


