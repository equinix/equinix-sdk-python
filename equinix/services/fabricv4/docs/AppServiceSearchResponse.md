# AppServiceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppService]**](AppService.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_search_response import AppServiceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceSearchResponse from a JSON string
app_service_search_response_instance = AppServiceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppServiceSearchResponse.to_json())

# convert the object into a dict
app_service_search_response_dict = app_service_search_response_instance.to_dict()
# create an instance of AppServiceSearchResponse from a dict
app_service_search_response_from_dict = AppServiceSearchResponse.from_dict(app_service_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


