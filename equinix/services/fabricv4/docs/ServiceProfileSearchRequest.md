# ServiceProfileSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ServiceProfileFilter**](ServiceProfileFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[ServiceProfileSortCriteria]**](ServiceProfileSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_search_request import ServiceProfileSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileSearchRequest from a JSON string
service_profile_search_request_instance = ServiceProfileSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileSearchRequest.to_json())

# convert the object into a dict
service_profile_search_request_dict = service_profile_search_request_instance.to_dict()
# create an instance of ServiceProfileSearchRequest from a dict
service_profile_search_request_form_dict = service_profile_search_request.from_dict(service_profile_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


