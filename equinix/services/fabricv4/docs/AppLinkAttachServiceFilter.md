# AppLinkAttachServiceFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Possible field names to use on filters:   * &#x60;/uuid&#x60; - App Service attach to App Link uuid   * &#x60;/attachmentStatus&#x60; - App Service attach to App Link status  | [optional] 
**operator** | **str** | Possible operators to use on filters:   * &#x60;&#x3D;&#x60; - equal   * &#x60;!&#x3D;&#x60; - not equal   * &#x60;IN&#x60; - in   * &#x60;NOT IN&#x60; - not in  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[AppLinkAttachServiceSimpleExpression]**](AppLinkAttachServiceSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attach_service_filter import AppLinkAttachServiceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachServiceFilter from a JSON string
app_link_attach_service_filter_instance = AppLinkAttachServiceFilter.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachServiceFilter.to_json())

# convert the object into a dict
app_link_attach_service_filter_dict = app_link_attach_service_filter_instance.to_dict()
# create an instance of AppLinkAttachServiceFilter from a dict
app_link_attach_service_filter_from_dict = AppLinkAttachServiceFilter.from_dict(app_link_attach_service_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


