# VrfBGPNeighbors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_neighbors** | [**List[VrfBGPNeighborsBgpNeighborsInner]**](VrfBGPNeighborsBgpNeighborsInner.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_bgp_neighbors import VrfBGPNeighbors

# TODO update the JSON string below
json = "{}"
# create an instance of VrfBGPNeighbors from a JSON string
vrf_bgp_neighbors_instance = VrfBGPNeighbors.from_json(json)
# print the JSON string representation of the object
print(VrfBGPNeighbors.to_json())

# convert the object into a dict
vrf_bgp_neighbors_dict = vrf_bgp_neighbors_instance.to_dict()
# create an instance of VrfBGPNeighbors from a dict
vrf_bgp_neighbors_form_dict = vrf_bgp_neighbors.from_dict(vrf_bgp_neighbors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


