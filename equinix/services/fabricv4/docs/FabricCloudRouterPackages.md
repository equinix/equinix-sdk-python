# FabricCloudRouterPackages

Cloud Router  package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**FabricCloudRouterCode**](FabricCloudRouterCode.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_cloud_router_packages import FabricCloudRouterPackages

# TODO update the JSON string below
json = "{}"
# create an instance of FabricCloudRouterPackages from a JSON string
fabric_cloud_router_packages_instance = FabricCloudRouterPackages.from_json(json)
# print the JSON string representation of the object
print(FabricCloudRouterPackages.to_json())

# convert the object into a dict
fabric_cloud_router_packages_dict = fabric_cloud_router_packages_instance.to_dict()
# create an instance of FabricCloudRouterPackages from a dict
fabric_cloud_router_packages_from_dict = FabricCloudRouterPackages.from_dict(fabric_cloud_router_packages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


