# PortPackage

Port Package details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Port Package URI | [optional] [readonly] 
**type** | [**PortPackageType**](PortPackageType.md) |  | 
**code** | **str** | Port Package code | 
**vc_bandwidth_max** | **int** | Maximum virtual connection bandwidth in Mbps | [optional] 
**vc_remote_supported** | **bool** | Indicates if remote virtual connections are supported | [optional] 
**supported_service_types** | [**List[PortPackageSupportedServiceTypesInner]**](PortPackageSupportedServiceTypesInner.md) | List of supported service types | [optional] 
**supported_source_types** | [**List[PortPackageSourceType]**](PortPackageSourceType.md) | List of supported source types | [optional] 
**supported_metros** | **List[str]** | List of supported metros | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_package import PortPackage

# TODO update the JSON string below
json = "{}"
# create an instance of PortPackage from a JSON string
port_package_instance = PortPackage.from_json(json)
# print the JSON string representation of the object
print(PortPackage.to_json())

# convert the object into a dict
port_package_dict = port_package_instance.to_dict()
# create an instance of PortPackage from a dict
port_package_from_dict = PortPackage.from_dict(port_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


