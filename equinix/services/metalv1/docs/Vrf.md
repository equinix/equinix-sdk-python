# Vrf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_dynamic_neighbors_bfd_enabled** | **bool** | Toggle BFD on dynamic bgp neighbors sessions | [optional] 
**bgp_dynamic_neighbors_enabled** | **bool** | Toggle to enable the dynamic bgp neighbors feature on the VRF | [optional] 
**bgp_dynamic_neighbors_export_route_map** | **bool** | Toggle to export the VRF route-map to the dynamic bgp neighbors | [optional] 
**bill** | **bool** | True if the VRF is being billed. Usage will start when the first VRF Virtual Circuit is active, and will only stop when the VRF has been deleted. | [optional] [default to False]
**created_at** | **datetime** |  | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**description** | **str** | Optional field that can be set to describe the VRF | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_ranges** | **List[str]** | A list of CIDR network addresses. Like [\&quot;10.0.0.0/16\&quot;, \&quot;2001:d78::/59\&quot;]. | [optional] 
**local_asn** | **int** | A 4-byte ASN associated with the VRF. | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**name** | **str** |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_circuits** | [**List[VrfVirtualCircuit]**](VrfVirtualCircuit.md) | Virtual circuits that are in the VRF | [optional] 

## Example

```python
from equinix_metal.models.vrf import Vrf

# TODO update the JSON string below
json = "{}"
# create an instance of Vrf from a JSON string
vrf_instance = Vrf.from_json(json)
# print the JSON string representation of the object
print(Vrf.to_json())

# convert the object into a dict
vrf_dict = vrf_instance.to_dict()
# create an instance of Vrf from a dict
vrf_form_dict = vrf.from_dict(vrf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


