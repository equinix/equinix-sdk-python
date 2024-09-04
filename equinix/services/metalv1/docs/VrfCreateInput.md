# VrfCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_dynamic_neighbors_bfd_enabled** | **bool** | Toggle BFD on dynamic bgp neighbors sessions | [optional] 
**bgp_dynamic_neighbors_enabled** | **bool** | Toggle to enable the dynamic bgp neighbors feature on the VRF | [optional] 
**bgp_dynamic_neighbors_export_route_map** | **bool** | Toggle to export the VRF route-map to the dynamic bgp neighbors | [optional] 
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**ip_ranges** | **List[str]** | A list of CIDR network addresses. Like [\&quot;10.0.0.0/16\&quot;, \&quot;2001:d78::/59\&quot;]. IPv4 blocks must be between /8 and /29 in size. IPv6 blocks must be between /59 and /64. A VRF\\&#39;s IP ranges must be defined in order to create VRF IP Reservations, which can then be used for Metal Gateways or Virtual Circuits. | [optional] 
**local_asn** | **int** |  | [optional] 
**metro** | **str** | The UUID (or metro code) for the Metro in which to create this VRF. | 
**name** | **str** |  | 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_create_input import VrfCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfCreateInput from a JSON string
vrf_create_input_instance = VrfCreateInput.from_json(json)
# print the JSON string representation of the object
print(VrfCreateInput.to_json())

# convert the object into a dict
vrf_create_input_dict = vrf_create_input_instance.to_dict()
# create an instance of VrfCreateInput from a dict
vrf_create_input_form_dict = vrf_create_input.from_dict(vrf_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


