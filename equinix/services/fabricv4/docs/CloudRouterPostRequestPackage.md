# CloudRouterPostRequestPackage

Fabric Cloud Router Package Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Fabric Cloud Router URI | [optional] 
**type** | [**CloudRouterPostRequestPackageType**](CloudRouterPostRequestPackageType.md) |  | [optional] 
**code** | [**CloudRouterPostRequestPackageCode**](CloudRouterPostRequestPackageCode.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_post_request_package import CloudRouterPostRequestPackage

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterPostRequestPackage from a JSON string
cloud_router_post_request_package_instance = CloudRouterPostRequestPackage.from_json(json)
# print the JSON string representation of the object
print(CloudRouterPostRequestPackage.to_json())

# convert the object into a dict
cloud_router_post_request_package_dict = cloud_router_post_request_package_instance.to_dict()
# create an instance of CloudRouterPostRequestPackage from a dict
cloud_router_post_request_package_form_dict = cloud_router_post_request_package.from_dict(cloud_router_post_request_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


