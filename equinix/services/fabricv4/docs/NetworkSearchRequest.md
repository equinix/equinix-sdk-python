# NetworkSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**NetworkFilter**](NetworkFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[NetworkSortCriteria]**](NetworkSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.network_search_request import NetworkSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSearchRequest from a JSON string
network_search_request_instance = NetworkSearchRequest.from_json(json)
# print the JSON string representation of the object
print(NetworkSearchRequest.to_json())

# convert the object into a dict
network_search_request_dict = network_search_request_instance.to_dict()
# create an instance of NetworkSearchRequest from a dict
network_search_request_from_dict = NetworkSearchRequest.from_dict(network_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


