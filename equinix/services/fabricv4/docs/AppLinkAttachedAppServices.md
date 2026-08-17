# AppLinkAttachedAppServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppLinkAttachedAppService]**](AppLinkAttachedAppService.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attached_app_services import AppLinkAttachedAppServices

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachedAppServices from a JSON string
app_link_attached_app_services_instance = AppLinkAttachedAppServices.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachedAppServices.to_json())

# convert the object into a dict
app_link_attached_app_services_dict = app_link_attached_app_services_instance.to_dict()
# create an instance of AppLinkAttachedAppServices from a dict
app_link_attached_app_services_from_dict = AppLinkAttachedAppServices.from_dict(app_link_attached_app_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


