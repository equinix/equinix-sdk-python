# CrossConnectSearchRequest

Search Cross Connects based on filter criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CrossConnectSearchFilters**](CrossConnectSearchFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[CrossConnectSortCriteria]**](CrossConnectSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_search_request import CrossConnectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectSearchRequest from a JSON string
cross_connect_search_request_instance = CrossConnectSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CrossConnectSearchRequest.to_json())

# convert the object into a dict
cross_connect_search_request_dict = cross_connect_search_request_instance.to_dict()
# create an instance of CrossConnectSearchRequest from a dict
cross_connect_search_request_from_dict = CrossConnectSearchRequest.from_dict(cross_connect_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


