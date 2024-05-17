# VrfUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_dynamic_neighbors_bfd_enabled** | **bool** | Toggle BFD on dynamic bgp neighbors sessions | [optional] 
**bgp_dynamic_neighbors_enabled** | **bool** | Toggle to enable the dynamic bgp neighbors feature on the VRF | [optional] 
**bgp_dynamic_neighbors_export_route_map** | **bool** | Toggle to export the VRF route-map to the dynamic bgp neighbors | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**ip_ranges** | **List[str]** | A list of CIDR network addresses. Like [\&quot;10.0.0.0/16\&quot;, \&quot;2001:d78::/56\&quot;]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /56 and /64. A VRF\\&#39;s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits. Adding a new CIDR address to the list will result in the creation of a new IP Range for this VRF. Removal of an existing CIDR address from the list will result in the deletion of an existing IP Range for this VRF. Deleting an IP Range will result in the deletion of any VRF IP Reservations contained within the IP Range, as well as the VRF IP Reservation\\&#39;s associated Metal Gateways or Virtual Circuits. If you do not wish to add or remove IP Ranges, either include the full existing list of IP Ranges in the update request, or do not specify the &#x60;ip_ranges&#x60; field in the update request. Specifying a value of &#x60;[]&#x60; will remove all existing IP Ranges from the VRF. | [optional] 
**local_asn** | **int** | The new &#x60;local_asn&#x60; value for the VRF. This field cannot be updated when there are active Interconnection Virtual Circuits associated to the VRF, or if any of the VLANs of the VRF&#39;s metal gateway has been assigned on an instance. | [optional] 
**name** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_update_input import VrfUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfUpdateInput from a JSON string
vrf_update_input_instance = VrfUpdateInput.from_json(json)
# print the JSON string representation of the object
print(VrfUpdateInput.to_json())

# convert the object into a dict
vrf_update_input_dict = vrf_update_input_instance.to_dict()
# create an instance of VrfUpdateInput from a dict
vrf_update_input_form_dict = vrf_update_input.from_dict(vrf_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


