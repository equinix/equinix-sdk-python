# VirtualCircuitUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**speed** | **str** | Speed can be changed only if it is an interconnection on a Dedicated Port | [optional] 
**tags** | **List[str]** |  | [optional] 
**vnid** | **str** | A Virtual Network record UUID or the VNID of a Metro Virtual Network in your project. | [optional] 
**customer_ip** | **str** | An IPv4 address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**customer_ipv6** | **str** | An IPv6 address from the subnet IPv6 that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet IPv6 as the Metal IPv6. By default, the last usable IP address in the subnet IPv6 will be used. | [optional] 
**md5** | **str** | The plaintext BGP peering password shared by neighbors as an MD5 checksum: * must be 10-20 characters long * may not include punctuation * must be a combination of numbers and letters * must contain at least one lowercase, uppercase, and digit character  | [optional] 
**metal_ip** | **str** | An IPv4 address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**metal_ipv6** | **str** | An IPv6 address from the subnet IPv6 that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IPv6 address in the subnet IPv6 as the Customer IP. By default, the first usable IPv6 address in the subnet IPv6 will be used. | [optional] 
**peer_asn** | **int** | The peer ASN that will be used with the VRF on the Virtual Circuit. | [optional] 
**subnet** | **str** | The /30 or /31 IPv4 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. | [optional] 
**subnet_ipv6** | **str** | The /126 or /127 IPv6 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IPv6 and Customer IPv6 must be IPs from this subnet. For /126 subnets, the network and broadcast IPs cannot be used as the Metal IPv6 or Customer IPv6. The subnet specified must be contained within an already-defined IP Range for the VRF. | [optional] 

## Example

```python
from equinix_metal.models.virtual_circuit_update_input import VirtualCircuitUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCircuitUpdateInput from a JSON string
virtual_circuit_update_input_instance = VirtualCircuitUpdateInput.from_json(json)
# print the JSON string representation of the object
print(VirtualCircuitUpdateInput.to_json())

# convert the object into a dict
virtual_circuit_update_input_dict = virtual_circuit_update_input_instance.to_dict()
# create an instance of VirtualCircuitUpdateInput from a dict
virtual_circuit_update_input_form_dict = virtual_circuit_update_input.from_dict(virtual_circuit_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


