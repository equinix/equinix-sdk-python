# AppLinkAttachProcessorFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/uuid&#x60; - App Processor attach to App Link uuid   * &#x60;/attachmentStatus&#x60; - App Processor attach to App Link status  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[AppLinkAttachProcessorSimpleExpression]**](AppLinkAttachProcessorSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_processor_filter import AppLinkAttachProcessorFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachProcessorFilter from a JSON string
app_link_attach_processor_filter_instance = AppLinkAttachProcessorFilter.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachProcessorFilter.to_json())

# convert the object into a dict
app_link_attach_processor_filter_dict = app_link_attach_processor_filter_instance.to_dict()
# create an instance of AppLinkAttachProcessorFilter from a dict
app_link_attach_processor_filter_from_dict = AppLinkAttachProcessorFilter.from_dict(app_link_attach_processor_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


