# AppServiceAttachedAppLink

App Link object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] [readonly] 
**type** | [**AppLinkType**](AppLinkType.md) |  | [default to AppLinkType.APP_LINK]
**uuid** | **str** | Equinix-assigned access point identifier | 
**name** | **str** | Customer-provided App Link name | [optional] 
**description** | **str** | Customer-provided App Link description | [optional] 
**state** | [**AppLinkState**](AppLinkState.md) |  | [optional] 
**router** | [**AppLinkCloudRouter**](AppLinkCloudRouter.md) |  | [optional] 
**ipv4_address** | **str** | App Link IP address | [optional] 
**bandwidth** | **int** | App Link aggregated data transfer capacity in Mbps | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_attached_app_link import AppServiceAttachedAppLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceAttachedAppLink from a JSON string
app_service_attached_app_link_instance = AppServiceAttachedAppLink.from_json(json)
# print the JSON string representation of the object
print(AppServiceAttachedAppLink.to_json())

# convert the object into a dict
app_service_attached_app_link_dict = app_service_attached_app_link_instance.to_dict()
# create an instance of AppServiceAttachedAppLink from a dict
app_service_attached_app_link_from_dict = AppServiceAttachedAppLink.from_dict(app_service_attached_app_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


