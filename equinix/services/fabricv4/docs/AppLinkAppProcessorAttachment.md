# AppLinkAppProcessorAttachment

App Link Attached App Processor object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppProcessorType**](AppProcessorType.md) |  | [optional] [default to AppProcessorType.APP_PROCESSOR]
**uuid** | **str** | App Processor UUID | 
**config** | **bytearray** | Base64-encoded configuration for the processor attachment | [optional] 
**endpoint** | **str** | Endpoint DNS name assigned to the attached App Processor | [optional] 
**attachment_status** | [**AppLinkAttachState**](AppLinkAttachState.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_app_processor_attachment import AppLinkAppProcessorAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAppProcessorAttachment from a JSON string
app_link_app_processor_attachment_instance = AppLinkAppProcessorAttachment.from_json(json)
# print the JSON string representation of the object
print(AppLinkAppProcessorAttachment.to_json())

# convert the object into a dict
app_link_app_processor_attachment_dict = app_link_app_processor_attachment_instance.to_dict()
# create an instance of AppLinkAppProcessorAttachment from a dict
app_link_app_processor_attachment_from_dict = AppLinkAppProcessorAttachment.from_dict(app_link_app_processor_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


