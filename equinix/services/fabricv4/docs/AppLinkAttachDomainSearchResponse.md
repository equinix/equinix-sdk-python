# AppLinkAttachDomainSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppLinkAppDomainAttachment]**](AppLinkAppDomainAttachment.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_domain_search_response import AppLinkAttachDomainSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachDomainSearchResponse from a JSON string
app_link_attach_domain_search_response_instance = AppLinkAttachDomainSearchResponse.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachDomainSearchResponse.to_json())

# convert the object into a dict
app_link_attach_domain_search_response_dict = app_link_attach_domain_search_response_instance.to_dict()
# create an instance of AppLinkAttachDomainSearchResponse from a dict
app_link_attach_domain_search_response_from_dict = AppLinkAttachDomainSearchResponse.from_dict(app_link_attach_domain_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


