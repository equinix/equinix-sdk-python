# AppLinkAttachProcessorRequest

Attach App Processor to App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **bytearray** | Base64-encoded configuration for the processor attachment | 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_processor_request import AppLinkAttachProcessorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachProcessorRequest from a JSON string
app_link_attach_processor_request_instance = AppLinkAttachProcessorRequest.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachProcessorRequest.to_json())

# convert the object into a dict
app_link_attach_processor_request_dict = app_link_attach_processor_request_instance.to_dict()
# create an instance of AppLinkAttachProcessorRequest from a dict
app_link_attach_processor_request_from_dict = AppLinkAttachProcessorRequest.from_dict(app_link_attach_processor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


