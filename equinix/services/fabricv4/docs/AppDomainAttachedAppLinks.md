# AppDomainAttachedAppLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppDomainAttachedAppLink]**](AppDomainAttachedAppLink.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_attached_app_links import AppDomainAttachedAppLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainAttachedAppLinks from a JSON string
app_domain_attached_app_links_instance = AppDomainAttachedAppLinks.from_json(json)
# print the JSON string representation of the object
print(AppDomainAttachedAppLinks.to_json())

# convert the object into a dict
app_domain_attached_app_links_dict = app_domain_attached_app_links_instance.to_dict()
# create an instance of AppDomainAttachedAppLinks from a dict
app_domain_attached_app_links_from_dict = AppDomainAttachedAppLinks.from_dict(app_domain_attached_app_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


