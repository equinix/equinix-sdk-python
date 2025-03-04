# VrfVirtualCircuitCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ip** | **str** | An IPv4 address from the subnet that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Metal IP. By default, the last usable IP address in the subnet will be used. | [optional] 
**customer_ipv6** | **str** | An IPv6 address from the subnet IPv6 that will be used on the Customer side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet IPv6 as the Metal IPv6. By default, the last usable IP address in the subnet IPv6 will be used. | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**md5** | **str** | The plaintext BGP peering password shared by neighbors as an MD5 checksum: * must be 10-20 characters long * may not include punctuation * must be a combination of numbers and letters * must contain at least one lowercase, uppercase, and digit character  | [optional] 
**metal_ip** | **str** | An IPv4 address from the subnet that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IP address in the subnet as the Customer IP. By default, the first usable IP address in the subnet will be used. | [optional] 
**metal_ipv6** | **str** | An IPv6 address from the subnet IPv6 that will be used on the Metal side. This parameter is optional, but if supplied, we will use the other usable IPv6 address in the subnet IPv6 as the Customer IP. By default, the first usable IPv6 address in the subnet IPv6 will be used. | [optional] 
**name** | **str** |  | [optional] 
**nni_vlan** | **int** |  | 
**peer_asn** | **int** | The peer ASN that will be used with the VRF on the Virtual Circuit. | 
**project_id** | **str** |  | 
**speed** | **str** | speed can be passed as integer number representing bps speed or string (e.g. &#39;52m&#39; or &#39;100g&#39; or &#39;4 gbps&#39;) | [optional] 
**subnet** | **str** | The /30 or /31 IPv4 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IP and Customer IP must be IPs from this subnet. For /30 subnets, the network and broadcast IPs cannot be used as the Metal or Customer IP. The subnet specified must be contained within an already-defined IP Range for the VRF. | 
**subnet_ipv6** | **str** | The /126 or /127 IPv6 subnet of one of the VRF IP Blocks that will be used with the VRF for the Virtual Circuit. This subnet does not have to be an existing VRF IP reservation, as we will create the VRF IP reservation on creation if it does not exist. The Metal IPv6 and Customer IPv6 must be IPs from this subnet. For /126 subnets, the network and broadcast IPs cannot be used as the Metal IPv6 or Customer IPv6. The subnet specified must be contained within an already-defined IP Range for the VRF. | [optional] 
**tags** | **List[str]** |  | [optional] 
**vrf** | **str** | The UUID of the VRF that will be associated with the Virtual Circuit. | 

## Example

```python
from equinix.services.metalv1.models.vrf_virtual_circuit_create_input import VrfVirtualCircuitCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfVirtualCircuitCreateInput from a JSON string
vrf_virtual_circuit_create_input_instance = VrfVirtualCircuitCreateInput.from_json(json)
# print the JSON string representation of the object
print(VrfVirtualCircuitCreateInput.to_json())

# convert the object into a dict
vrf_virtual_circuit_create_input_dict = vrf_virtual_circuit_create_input_instance.to_dict()
# create an instance of VrfVirtualCircuitCreateInput from a dict
vrf_virtual_circuit_create_input_from_dict = VrfVirtualCircuitCreateInput.from_dict(vrf_virtual_circuit_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


