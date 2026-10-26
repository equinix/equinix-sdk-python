# AppLinkAttachProcessorFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppLinkAttachProcessorFilter]**](AppLinkAttachProcessorFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_processor_filters import AppLinkAttachProcessorFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachProcessorFilters from a JSON string
app_link_attach_processor_filters_instance = AppLinkAttachProcessorFilters.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachProcessorFilters.to_json())

# convert the object into a dict
app_link_attach_processor_filters_dict = app_link_attach_processor_filters_instance.to_dict()
# create an instance of AppLinkAttachProcessorFilters from a dict
app_link_attach_processor_filters_from_dict = AppLinkAttachProcessorFilters.from_dict(app_link_attach_processor_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


