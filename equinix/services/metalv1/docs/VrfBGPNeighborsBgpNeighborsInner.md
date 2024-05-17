# VrfBGPNeighborsBgpNeighborsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_as** | **int** | The ASN of the peer that advertised the prefix. | [optional] 
**peer_ip** | **str** |  | [optional] 
**state** | **str** | The current status of the connection to the BGP peer. State is either up or down. | [optional] 

## Example

```python
from equinix_metal.models.vrf_bgp_neighbors_bgp_neighbors_inner import VrfBGPNeighborsBgpNeighborsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VrfBGPNeighborsBgpNeighborsInner from a JSON string
vrf_bgp_neighbors_bgp_neighbors_inner_instance = VrfBGPNeighborsBgpNeighborsInner.from_json(json)
# print the JSON string representation of the object
print(VrfBGPNeighborsBgpNeighborsInner.to_json())

# convert the object into a dict
vrf_bgp_neighbors_bgp_neighbors_inner_dict = vrf_bgp_neighbors_bgp_neighbors_inner_instance.to_dict()
# create an instance of VrfBGPNeighborsBgpNeighborsInner from a dict
vrf_bgp_neighbors_bgp_neighbors_inner_form_dict = vrf_bgp_neighbors_bgp_neighbors_inner.from_dict(vrf_bgp_neighbors_bgp_neighbors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


