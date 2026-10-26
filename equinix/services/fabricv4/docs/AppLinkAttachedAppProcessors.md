# AppLinkAttachedAppProcessors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[AppLinkAppProcessorAttachment]**](AppLinkAppProcessorAttachment.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attached_app_processors import AppLinkAttachedAppProcessors

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachedAppProcessors from a JSON string
app_link_attached_app_processors_instance = AppLinkAttachedAppProcessors.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachedAppProcessors.to_json())

# convert the object into a dict
app_link_attached_app_processors_dict = app_link_attached_app_processors_instance.to_dict()
# create an instance of AppLinkAttachedAppProcessors from a dict
app_link_attached_app_processors_from_dict = AppLinkAttachedAppProcessors.from_dict(app_link_attached_app_processors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


