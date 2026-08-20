# AppLinkAppDomainAttachment

App Link Attached App Domain object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppDomainType**](AppDomainType.md) |  | [optional] [default to AppDomainType.APP_DOMAIN]
**uuid** | **str** | Equinix-assigned access point identifier | 
**name** | **str** | Customer-provided App Domain name | [optional] 
**attachment_status** | [**AppLinkAttachState**](AppLinkAttachState.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_app_domain_attachment import AppLinkAppDomainAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAppDomainAttachment from a JSON string
app_link_app_domain_attachment_instance = AppLinkAppDomainAttachment.from_json(json)
# print the JSON string representation of the object
print(AppLinkAppDomainAttachment.to_json())

# convert the object into a dict
app_link_app_domain_attachment_dict = app_link_app_domain_attachment_instance.to_dict()
# create an instance of AppLinkAppDomainAttachment from a dict
app_link_app_domain_attachment_from_dict = AppLinkAppDomainAttachment.from_dict(app_link_app_domain_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


