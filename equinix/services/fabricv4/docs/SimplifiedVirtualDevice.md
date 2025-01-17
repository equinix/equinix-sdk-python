# SimplifiedVirtualDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | url to entity | [optional] 
**uuid** | **str** | Network Edge assigned Virtual Device Identifier | [optional] 
**type** | [**SimplifiedVirtualDeviceType**](SimplifiedVirtualDeviceType.md) |  | [optional] 
**name** | **str** | Customer-assigned Virtual Device name | [optional] 
**cluster** | **str** | Virtual Device Cluster Information | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_virtual_device import SimplifiedVirtualDevice

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedVirtualDevice from a JSON string
simplified_virtual_device_instance = SimplifiedVirtualDevice.from_json(json)
# print the JSON string representation of the object
print(SimplifiedVirtualDevice.to_json())

# convert the object into a dict
simplified_virtual_device_dict = simplified_virtual_device_instance.to_dict()
# create an instance of SimplifiedVirtualDevice from a dict
simplified_virtual_device_from_dict = SimplifiedVirtualDevice.from_dict(simplified_virtual_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


