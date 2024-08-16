# TimeServicesSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TimeServiceFilters**](TimeServiceFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[TimeServiceSortCriteria]**](TimeServiceSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_services_search_request import TimeServicesSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServicesSearchRequest from a JSON string
time_services_search_request_instance = TimeServicesSearchRequest.from_json(json)
# print the JSON string representation of the object
print(TimeServicesSearchRequest.to_json())

# convert the object into a dict
time_services_search_request_dict = time_services_search_request_instance.to_dict()
# create an instance of TimeServicesSearchRequest from a dict
time_services_search_request_form_dict = time_services_search_request.from_dict(time_services_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


