# VirtualPortLocation

Geographic data for the port.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ibx** | **str** | Code assigned to the Equinix International Business Exchange (IBX) data center from which the port is ordered. &lt;br&gt; The port might be in a different location. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_port_location import VirtualPortLocation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPortLocation from a JSON string
virtual_port_location_instance = VirtualPortLocation.from_json(json)
# print the JSON string representation of the object
print(VirtualPortLocation.to_json())

# convert the object into a dict
virtual_port_location_dict = virtual_port_location_instance.to_dict()
# create an instance of VirtualPortLocation from a dict
virtual_port_location_from_dict = VirtualPortLocation.from_dict(virtual_port_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


