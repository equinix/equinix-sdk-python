# AppLinkSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppLinkFilters**](AppLinkFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppLinkSortCriteria]**](AppLinkSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_search_request import AppLinkSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkSearchRequest from a JSON string
app_link_search_request_instance = AppLinkSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkSearchRequest.to_json())

# convert the object into a dict
app_link_search_request_dict = app_link_search_request_instance.to_dict()
# create an instance of AppLinkSearchRequest from a dict
app_link_search_request_from_dict = AppLinkSearchRequest.from_dict(app_link_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


