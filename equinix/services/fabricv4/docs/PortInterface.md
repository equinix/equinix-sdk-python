# PortInterface

Port interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Port interface type | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_interface import PortInterface

# TODO update the JSON string below
json = "{}"
# create an instance of PortInterface from a JSON string
port_interface_instance = PortInterface.from_json(json)
# print the JSON string representation of the object
print(PortInterface.to_json())

# convert the object into a dict
port_interface_dict = port_interface_instance.to_dict()
# create an instance of PortInterface from a dict
port_interface_from_dict = PortInterface.from_dict(port_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


