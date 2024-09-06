# VpicInterface

MCN VPIC Interface Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Canonical URL at which the resource resides. | [optional] [readonly] 
**uuid** | **str** | MCN assigned VPIC Interface Identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.vpic_interface import VpicInterface

# TODO update the JSON string below
json = "{}"
# create an instance of VpicInterface from a JSON string
vpic_interface_instance = VpicInterface.from_json(json)
# print the JSON string representation of the object
print(VpicInterface.to_json())

# convert the object into a dict
vpic_interface_dict = vpic_interface_instance.to_dict()
# create an instance of VpicInterface from a dict
vpic_interface_from_dict = VpicInterface.from_dict(vpic_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


