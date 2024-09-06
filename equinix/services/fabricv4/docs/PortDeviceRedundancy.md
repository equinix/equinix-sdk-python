# PortDeviceRedundancy

Device redundancy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Device redundancy group | [optional] 
**priority** | [**PortDeviceRedundancyPriority**](PortDeviceRedundancyPriority.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_device_redundancy import PortDeviceRedundancy

# TODO update the JSON string below
json = "{}"
# create an instance of PortDeviceRedundancy from a JSON string
port_device_redundancy_instance = PortDeviceRedundancy.from_json(json)
# print the JSON string representation of the object
print(PortDeviceRedundancy.to_json())

# convert the object into a dict
port_device_redundancy_dict = port_device_redundancy_instance.to_dict()
# create an instance of PortDeviceRedundancy from a dict
port_device_redundancy_from_dict = PortDeviceRedundancy.from_dict(port_device_redundancy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


