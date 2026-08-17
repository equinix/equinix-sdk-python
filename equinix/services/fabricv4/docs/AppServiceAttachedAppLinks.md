# AppServiceAttachedAppLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppServiceAttachedAppLink]**](AppServiceAttachedAppLink.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_links import AppServiceAttachedAppLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppLinks from a JSON string
app_service_attached_app_links_instance = AppServiceAttachedAppLinks.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppLinks.to_json())

# convert the object into a dict
app_service_attached_app_links_dict = app_service_attached_app_links_instance.to_dict()
# create an instance of AppServiceAttachedAppLinks from a dict
app_service_attached_app_links_from_dict = AppServiceAttachedAppLinks.from_dict(app_service_attached_app_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


