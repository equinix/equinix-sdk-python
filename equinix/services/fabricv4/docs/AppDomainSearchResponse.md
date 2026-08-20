# AppDomainSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppDomain]**](AppDomain.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_search_response import AppDomainSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainSearchResponse from a JSON string
app_domain_search_response_instance = AppDomainSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppDomainSearchResponse.to_json())

# convert the object into a dict
app_domain_search_response_dict = app_domain_search_response_instance.to_dict()
# create an instance of AppDomainSearchResponse from a dict
app_domain_search_response_from_dict = AppDomainSearchResponse.from_dict(app_domain_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


