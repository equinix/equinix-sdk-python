# PortTether

Port physical connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cross_connect_id** | **str** | Port cross connect identifier | [optional] 
**cabinet_number** | **str** | Port cabinet number | [optional] 
**system_name** | **str** | Port system name | [optional] 
**patch_panel** | **str** | Port patch panel | [optional] 
**patch_panel_port_a** | **str** | Port patch panel port A | [optional] 
**patch_panel_port_b** | **str** | Port patch panel port B | [optional] 
**ibx** | **str** | z-side/Equinix IBX | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_tether import PortTether

# TODO update the JSON string below
json = "{}"
# create an instance of PortTether from a JSON string
port_tether_instance = PortTether.from_json(json)
# print the JSON string representation of the object
print(PortTether.to_json())

# convert the object into a dict
port_tether_dict = port_tether_instance.to_dict()
# create an instance of PortTether from a dict
port_tether_from_dict = PortTether.from_dict(port_tether_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


