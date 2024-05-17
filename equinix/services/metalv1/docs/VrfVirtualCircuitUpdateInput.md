# VrfVirtualCircuitUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ip** | **str** | An IP address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**md5** | **str** | The plaintext BGP peering password shared by neighbors as an MD5 checksum: * must be 10-20 characters long * may not include punctuation * must be a combination of numbers and letters * must contain at least one lowercase, uppercase, and digit character  | [optional] 
**metal_ip** | **str** | An IP address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**name** | **str** |  | [optional] 
**peer_asn** | **int** | The peer ASN that will be used with the VRF on the Virtual Circuit. | [optional] 
**speed** | **str** | Speed can be changed only if it is an interconnection on a Dedicated Port | [optional] 
**subnet** | **str** | The /30 or /31 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_virtual_circuit_update_input import VrfVirtualCircuitUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfVirtualCircuitUpdateInput from a JSON string
vrf_virtual_circuit_update_input_instance = VrfVirtualCircuitUpdateInput.from_json(json)
# print the JSON string representation of the object
print(VrfVirtualCircuitUpdateInput.to_json())

# convert the object into a dict
vrf_virtual_circuit_update_input_dict = vrf_virtual_circuit_update_input_instance.to_dict()
# create an instance of VrfVirtualCircuitUpdateInput from a dict
vrf_virtual_circuit_update_input_form_dict = vrf_virtual_circuit_update_input.from_dict(vrf_virtual_circuit_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


