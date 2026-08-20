# AppLinkAttachServiceSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppLinkAttachServiceFilters**](AppLinkAttachServiceFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppLinkAttachServiceSortCriteria]**](AppLinkAttachServiceSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_service_search_request import AppLinkAttachServiceSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachServiceSearchRequest from a JSON string
app_link_attach_service_search_request_instance = AppLinkAttachServiceSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachServiceSearchRequest.to_json())

# convert the object into a dict
app_link_attach_service_search_request_dict = app_link_attach_service_search_request_instance.to_dict()
# create an instance of AppLinkAttachServiceSearchRequest from a dict
app_link_attach_service_search_request_from_dict = AppLinkAttachServiceSearchRequest.from_dict(app_link_attach_service_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


