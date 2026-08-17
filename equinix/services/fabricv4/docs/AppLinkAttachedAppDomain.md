# AppLinkAttachedAppDomain

App Domain object associated with App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppDomainType**](AppDomainType.md) |  | [default to AppDomainType.APP_DOMAIN]
**uuid** | **str** | Equinix-assigned access point identifier | 
**name** | **str** | Customer-provided App Domain name | [optional] 
**description** | **str** | Customer-provided App Domain description | [optional] 
**state** | [**AppDomainState**](AppDomainState.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**attachment_status** | [**AppLinkAttachState**](AppLinkAttachState.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attached_app_domain import AppLinkAttachedAppDomain

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachedAppDomain from a JSON string
app_link_attached_app_domain_instance = AppLinkAttachedAppDomain.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachedAppDomain.to_json())

# convert the object into a dict
app_link_attached_app_domain_dict = app_link_attached_app_domain_instance.to_dict()
# create an instance of AppLinkAttachedAppDomain from a dict
app_link_attached_app_domain_from_dict = AppLinkAttachedAppDomain.from_dict(app_link_attached_app_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


