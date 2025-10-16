# VirtualPortPackage

Virtual Port Package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Virtual port package code | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_port_package import VirtualPortPackage

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPortPackage from a JSON string
virtual_port_package_instance = VirtualPortPackage.from_json(json)
# print the JSON string representation of the object
print(VirtualPortPackage.to_json())

# convert the object into a dict
virtual_port_package_dict = virtual_port_package_instance.to_dict()
# create an instance of VirtualPortPackage from a dict
virtual_port_package_from_dict = VirtualPortPackage.from_dict(virtual_port_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


