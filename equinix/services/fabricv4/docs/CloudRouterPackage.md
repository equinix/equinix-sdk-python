# CloudRouterPackage

Fabric Cloud Router Package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Cloud Router package URI | [optional] [readonly] 
**type** | [**CloudRouterPackageType**](CloudRouterPackageType.md) |  | [optional] 
**code** | [**Code**](Code.md) |  | [optional] 
**description** | **str** | Fabric Cloud Router Package description | [optional] 
**total_ipv4_routes_max** | **int** | Cloud Router package BGP IPv4 routes limit | [optional] 
**total_ipv6_routes_max** | **int** | Cloud Router package BGP IPv6 routes limit | [optional] 
**route_filter_supported** | **bool** | CloudRouter package route filter support | [optional] 
**vc_count_max** | **int** | CloudRouter package Max Connection limit | [optional] 
**cr_count_max** | **int** | CloudRouter package Max CloudRouter limit | [optional] 
**vc_bandwidth_max** | **int** | CloudRouter package Max Bandwidth limit | [optional] 
**change_log** | [**PackageChangeLog**](PackageChangeLog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_package import CloudRouterPackage

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterPackage from a JSON string
cloud_router_package_instance = CloudRouterPackage.from_json(json)
# print the JSON string representation of the object
print(CloudRouterPackage.to_json())

# convert the object into a dict
cloud_router_package_dict = cloud_router_package_instance.to_dict()
# create an instance of CloudRouterPackage from a dict
cloud_router_package_form_dict = cloud_router_package.from_dict(cloud_router_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


