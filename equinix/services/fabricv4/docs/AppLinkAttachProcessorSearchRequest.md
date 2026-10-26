# AppLinkAttachProcessorSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppLinkAttachProcessorFilters**](AppLinkAttachProcessorFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppLinkAttachProcessorSortCriteria]**](AppLinkAttachProcessorSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_processor_search_request import AppLinkAttachProcessorSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachProcessorSearchRequest from a JSON string
app_link_attach_processor_search_request_instance = AppLinkAttachProcessorSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachProcessorSearchRequest.to_json())

# convert the object into a dict
app_link_attach_processor_search_request_dict = app_link_attach_processor_search_request_instance.to_dict()
# create an instance of AppLinkAttachProcessorSearchRequest from a dict
app_link_attach_processor_search_request_from_dict = AppLinkAttachProcessorSearchRequest.from_dict(app_link_attach_processor_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


