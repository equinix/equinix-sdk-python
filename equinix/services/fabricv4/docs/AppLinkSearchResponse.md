# AppLinkSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppLink]**](AppLink.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_search_response import AppLinkSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkSearchResponse from a JSON string
app_link_search_response_instance = AppLinkSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppLinkSearchResponse.to_json())

# convert the object into a dict
app_link_search_response_dict = app_link_search_response_instance.to_dict()
# create an instance of AppLinkSearchResponse from a dict
app_link_search_response_from_dict = AppLinkSearchResponse.from_dict(app_link_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


