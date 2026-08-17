# AppLinkAttachServiceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppLinkAttachServiceFilter]**](AppLinkAttachServiceFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_service_filters import AppLinkAttachServiceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachServiceFilters from a JSON string
app_link_attach_service_filters_instance = AppLinkAttachServiceFilters.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachServiceFilters.to_json())

# convert the object into a dict
app_link_attach_service_filters_dict = app_link_attach_service_filters_instance.to_dict()
# create an instance of AppLinkAttachServiceFilters from a dict
app_link_attach_service_filters_from_dict = AppLinkAttachServiceFilters.from_dict(app_link_attach_service_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


