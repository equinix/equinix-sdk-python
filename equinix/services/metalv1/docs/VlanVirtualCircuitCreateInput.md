# VlanVirtualCircuitCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nni_vlan** | **int** |  | [optional] 
**project_id** | **str** |  | 
**speed** | **str** | speed can be passed as integer number representing bps speed or string (e.g. &#39;52m&#39; or &#39;100g&#39; or &#39;4 gbps&#39;) | [optional] 
**tags** | **List[str]** |  | [optional] 
**vnid** | **str** | A Virtual Network record UUID or the VNID of a Metro Virtual Network in your project (sent as integer). | [optional] 

## Example

```python
from equinix_metal.models.vlan_virtual_circuit_create_input import VlanVirtualCircuitCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VlanVirtualCircuitCreateInput from a JSON string
vlan_virtual_circuit_create_input_instance = VlanVirtualCircuitCreateInput.from_json(json)
# print the JSON string representation of the object
print(VlanVirtualCircuitCreateInput.to_json())

# convert the object into a dict
vlan_virtual_circuit_create_input_dict = vlan_virtual_circuit_create_input_instance.to_dict()
# create an instance of VlanVirtualCircuitCreateInput from a dict
vlan_virtual_circuit_create_input_form_dict = vlan_virtual_circuit_create_input.from_dict(vlan_virtual_circuit_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


