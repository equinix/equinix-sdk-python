# AppLinkAttachDomainSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppLinkAttachDomainFilters**](AppLinkAttachDomainFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppLinkAttachDomainSortCriteria]**](AppLinkAttachDomainSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_domain_search_request import AppLinkAttachDomainSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachDomainSearchRequest from a JSON string
app_link_attach_domain_search_request_instance = AppLinkAttachDomainSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachDomainSearchRequest.to_json())

# convert the object into a dict
app_link_attach_domain_search_request_dict = app_link_attach_domain_search_request_instance.to_dict()
# create an instance of AppLinkAttachDomainSearchRequest from a dict
app_link_attach_domain_search_request_from_dict = AppLinkAttachDomainSearchRequest.from_dict(app_link_attach_domain_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


