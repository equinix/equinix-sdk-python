# AppLinkAttachDomainFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppLinkAttachDomainFilter]**](AppLinkAttachDomainFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_domain_filters import AppLinkAttachDomainFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachDomainFilters from a JSON string
app_link_attach_domain_filters_instance = AppLinkAttachDomainFilters.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachDomainFilters.to_json())

# convert the object into a dict
app_link_attach_domain_filters_dict = app_link_attach_domain_filters_instance.to_dict()
# create an instance of AppLinkAttachDomainFilters from a dict
app_link_attach_domain_filters_from_dict = AppLinkAttachDomainFilters.from_dict(app_link_attach_domain_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


