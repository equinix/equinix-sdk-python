# AppLinkAppServiceAttachment

App Link Attached App Service object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppServiceType**](AppServiceType.md) |  | [optional] [default to AppServiceType.APP_SERVICE]
**uuid** | **str** | Equinix-assigned access point identifier | 
**geo_scope** | **str** | Geo scope for the App Service | 
**destination_ip** | **str** | Target IP for forwarding API requests | 
**attachment_status** | [**AppLinkAttachState**](AppLinkAttachState.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 
**change** | [**AppLinkAppServiceAttachmentChange**](AppLinkAppServiceAttachmentChange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_app_service_attachment import AppLinkAppServiceAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAppServiceAttachment from a JSON string
app_link_app_service_attachment_instance = AppLinkAppServiceAttachment.from_json(json)
# print the JSON string representation of the object
print(AppLinkAppServiceAttachment.to_json())

# convert the object into a dict
app_link_app_service_attachment_dict = app_link_app_service_attachment_instance.to_dict()
# create an instance of AppLinkAppServiceAttachment from a dict
app_link_app_service_attachment_from_dict = AppLinkAppServiceAttachment.from_dict(app_link_app_service_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


