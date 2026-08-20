# InterconnectPackage

Interconnect Package details <font color=\"red\"> <sup color='red'>Beta</sup></font>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Interconnect Package URI | [optional] [readonly] 
**type** | **str** | Interconnect Package Type | 
**uuid** | **str** | Equinix-assigned Interconnect Package identifier | [optional] 
**code** | **str** | Interconnect Package code (e.g. LAB, BASIC, STANDARD, PREMIUM) | 
**description** | **str** | Interconnect Package description | [optional] 
**routes_max** | **int** | Maximum number of routes | [optional] 
**bandwidth_max** | **int** | Maximum bandwidth in Mbps | [optional] 
**is_remote** | **bool** | Authorization to connect remotely | [optional] 

## Example

```python
from equinix.services.fabricv4.models.interconnect_package import InterconnectPackage

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectPackage from a JSON string
interconnect_package_instance = InterconnectPackage.from_json(json)
# print the JSON string representation of the object
print(InterconnectPackage.to_json())

# convert the object into a dict
interconnect_package_dict = interconnect_package_instance.to_dict()
# create an instance of InterconnectPackage from a dict
interconnect_package_from_dict = InterconnectPackage.from_dict(interconnect_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


