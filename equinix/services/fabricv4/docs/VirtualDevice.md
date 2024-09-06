# VirtualDevice

Virtual Device AccessPoint Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Virtual Device URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned Virtual Device identifier | [optional] 
**name** | **str** | Customer-assigned Virtual Device name | [optional] 
**type** | [**VirtualDeviceType**](VirtualDeviceType.md) |  | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_device import VirtualDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDevice from a JSON string
virtual_device_instance = VirtualDevice.from_json(json)
# print the JSON string representation of the object
print(VirtualDevice.to_json())

# convert the object into a dict
virtual_device_dict = virtual_device_instance.to_dict()
# create an instance of VirtualDevice from a dict
virtual_device_from_dict = VirtualDevice.from_dict(virtual_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


