# VrfBGPNeighborsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_neighbors** | [**List[VrfBGPNeighbors]**](VrfBGPNeighbors.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_bgp_neighbors_list import VrfBGPNeighborsList

# TODO update the JSON string below
json = "{}"
# create an instance of VrfBGPNeighborsList from a JSON string
vrf_bgp_neighbors_list_instance = VrfBGPNeighborsList.from_json(json)
# print the JSON string representation of the object
print(VrfBGPNeighborsList.to_json())

# convert the object into a dict
vrf_bgp_neighbors_list_dict = vrf_bgp_neighbors_list_instance.to_dict()
# create an instance of VrfBGPNeighborsList from a dict
vrf_bgp_neighbors_list_form_dict = vrf_bgp_neighbors_list.from_dict(vrf_bgp_neighbors_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


