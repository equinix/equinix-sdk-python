# AppLinkCloudRouter

App Link Cloud Router

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Resource URI | [optional] 
**type** | [**AppLinkCloudRouterType**](AppLinkCloudRouterType.md) |  | [optional] 
**uuid** | **str** | Cloud Router UUID | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_link_cloud_router import AppLinkCloudRouter

# TODO update the JSON string below
json = "{}"
# create an instance of AppLinkCloudRouter from a JSON string
app_link_cloud_router_instance = AppLinkCloudRouter.from_json(json)
# print the JSON string representation of the object
print(AppLinkCloudRouter.to_json())

# convert the object into a dict
app_link_cloud_router_dict = app_link_cloud_router_instance.to_dict()
# create an instance of AppLinkCloudRouter from a dict
app_link_cloud_router_from_dict = AppLinkCloudRouter.from_dict(app_link_cloud_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


