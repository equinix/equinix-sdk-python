# AppProcessorSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**AppProcessorFilters**](AppProcessorFilters.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[AppProcessorSortCriteria]**](AppProcessorSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor_search_request import AppProcessorSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorSearchRequest from a JSON string
app_processor_search_request_instance = AppProcessorSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AppProcessorSearchRequest.to_json())

# convert the object into a dict
app_processor_search_request_dict = app_processor_search_request_instance.to_dict()
# create an instance of AppProcessorSearchRequest from a dict
app_processor_search_request_from_dict = AppProcessorSearchRequest.from_dict(app_processor_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


