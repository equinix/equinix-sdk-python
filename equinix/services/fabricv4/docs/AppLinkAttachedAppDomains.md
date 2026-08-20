# AppLinkAttachedAppDomains


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppLinkAttachedAppDomain]**](AppLinkAttachedAppDomain.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attached_app_domains import AppLinkAttachedAppDomains

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachedAppDomains from a JSON string
app_link_attached_app_domains_instance = AppLinkAttachedAppDomains.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachedAppDomains.to_json())

# convert the object into a dict
app_link_attached_app_domains_dict = app_link_attached_app_domains_instance.to_dict()
# create an instance of AppLinkAttachedAppDomains from a dict
app_link_attached_app_domains_from_dict = AppLinkAttachedAppDomains.from_dict(app_link_attached_app_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


