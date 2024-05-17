# VlanVirtualCircuitUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**speed** | **str** | Speed can be changed only if it is an interconnection on a Dedicated Port | [optional] 
**tags** | **List[str]** |  | [optional] 
**vnid** | **str** | A Virtual Network record UUID or the VNID of a Metro Virtual Network in your project. | [optional] 

## Example

```python
from equinix_metal.models.vlan_virtual_circuit_update_input import VlanVirtualCircuitUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VlanVirtualCircuitUpdateInput from a JSON string
vlan_virtual_circuit_update_input_instance = VlanVirtualCircuitUpdateInput.from_json(json)
# print the JSON string representation of the object
print(VlanVirtualCircuitUpdateInput.to_json())

# convert the object into a dict
vlan_virtual_circuit_update_input_dict = vlan_virtual_circuit_update_input_instance.to_dict()
# create an instance of VlanVirtualCircuitUpdateInput from a dict
vlan_virtual_circuit_update_input_form_dict = vlan_virtual_circuit_update_input.from_dict(vlan_virtual_circuit_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


