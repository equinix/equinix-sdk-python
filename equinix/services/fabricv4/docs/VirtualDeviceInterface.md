# VirtualDeviceInterface

Virtual Device Interface Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**VirtualDeviceInterfaceType**](VirtualDeviceInterfaceType.md) |  | [optional] 
**id** | **int** | Network Edge assigned identifier | [optional] 
**uuid** | **str** | Interface identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_device_interface import VirtualDeviceInterface

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceInterface from a JSON string
virtual_device_interface_instance = VirtualDeviceInterface.from_json(json)
# print the JSON string representation of the object
print(VirtualDeviceInterface.to_json())

# convert the object into a dict
virtual_device_interface_dict = virtual_device_interface_instance.to_dict()
# create an instance of VirtualDeviceInterface from a dict
virtual_device_interface_from_dict = VirtualDeviceInterface.from_dict(virtual_device_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


