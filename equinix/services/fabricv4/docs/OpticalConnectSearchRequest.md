# OpticalConnectSearchRequest

Search criteria for retrieving Optical Connects, with optional         filtering, pagination and sorting.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**OpticalConnectFilters**](OpticalConnectFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[OpticalConnectSortCriteria]**](OpticalConnectSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.optical_connect_search_request import OpticalConnectSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpticalConnectSearchRequest from a JSON string
optical_connect_search_request_instance = OpticalConnectSearchRequest.from_json(json)
# print the JSON string representation of the object
print(OpticalConnectSearchRequest.to_json())

# convert the object into a dict
optical_connect_search_request_dict = optical_connect_search_request_instance.to_dict()
# create an instance of OpticalConnectSearchRequest from a dict
optical_connect_search_request_from_dict = OpticalConnectSearchRequest.from_dict(optical_connect_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


