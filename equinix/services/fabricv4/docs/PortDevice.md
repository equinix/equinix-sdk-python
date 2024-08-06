# PortDevice

Port device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Device name | [optional] 
**redundancy** | [**PortDeviceRedundancy**](PortDeviceRedundancy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_device import PortDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PortDevice from a JSON string
port_device_instance = PortDevice.from_json(json)
# print the JSON string representation of the object
print(PortDevice.to_json())

# convert the object into a dict
port_device_dict = port_device_instance.to_dict()
# create an instance of PortDevice from a dict
port_device_from_dict = PortDevice.from_dict(port_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


