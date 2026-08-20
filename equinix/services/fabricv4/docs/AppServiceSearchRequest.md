# AppServiceSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppServiceFilters**](AppServiceFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppServiceSortCriteria]**](AppServiceSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_search_request import AppServiceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceSearchRequest from a JSON string
app_service_search_request_instance = AppServiceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppServiceSearchRequest.to_json())

# convert the object into a dict
app_service_search_request_dict = app_service_search_request_instance.to_dict()
# create an instance of AppServiceSearchRequest from a dict
app_service_search_request_from_dict = AppServiceSearchRequest.from_dict(app_service_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


