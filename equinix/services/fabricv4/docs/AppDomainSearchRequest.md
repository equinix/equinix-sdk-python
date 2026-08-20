# AppDomainSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppDomainFilters**](AppDomainFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppDomainSortCriteria]**](AppDomainSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_search_request import AppDomainSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainSearchRequest from a JSON string
app_domain_search_request_instance = AppDomainSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppDomainSearchRequest.to_json())

# convert the object into a dict
app_domain_search_request_dict = app_domain_search_request_instance.to_dict()
# create an instance of AppDomainSearchRequest from a dict
app_domain_search_request_from_dict = AppDomainSearchRequest.from_dict(app_domain_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


