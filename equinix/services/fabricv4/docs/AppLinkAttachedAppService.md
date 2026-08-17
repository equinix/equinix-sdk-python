# AppLinkAttachedAppService

App Service object associated with App Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppServiceType**](AppServiceType.md) |  | [default to AppServiceType.APP_SERVICE]
**uuid** | **str** | Equinix-assigned access point identifier | 
**name** | **str** | Customer-provided App Service name | [optional] 
**description** | **str** | Customer-provided App Service description | [optional] 
**state** | [**AppServiceState**](AppServiceState.md) |  | [optional] 
**endpoint** | **str** | Accessible endpoint through this service | [optional] 
**source_domains** | **List[str]** | List of source domains from where traffic is allowed | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**geo_scope** | **str** | Geo scope for the App Service | 
**destination_ip** | **str** | Target IP for forwarding API requests | 
**attachment_status** | [**AppLinkAttachState**](AppLinkAttachState.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_attached_app_service import AppLinkAttachedAppService

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkAttachedAppService from a JSON string
app_link_attached_app_service_instance = AppLinkAttachedAppService.from_json(json)
# print the JSON string representation of the object
print(AppLinkAttachedAppService.to_json())

# convert the object into a dict
app_link_attached_app_service_dict = app_link_attached_app_service_instance.to_dict()
# create an instance of AppLinkAttachedAppService from a dict
app_link_attached_app_service_from_dict = AppLinkAttachedAppService.from_dict(app_link_attached_app_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


