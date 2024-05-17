# BgpDynamicNeighborList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_dynamic_neighbors** | [**List[BgpDynamicNeighbor]**](BgpDynamicNeighbor.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_dynamic_neighbor_list import BgpDynamicNeighborList

# TODO update the JSON string below
json = "{}"
# create an instance of BgpDynamicNeighborList from a JSON string
bgp_dynamic_neighbor_list_instance = BgpDynamicNeighborList.from_json(json)
# print the JSON string representation of the object
print(BgpDynamicNeighborList.to_json())

# convert the object into a dict
bgp_dynamic_neighbor_list_dict = bgp_dynamic_neighbor_list_instance.to_dict()
# create an instance of BgpDynamicNeighborList from a dict
bgp_dynamic_neighbor_list_form_dict = bgp_dynamic_neighbor_list.from_dict(bgp_dynamic_neighbor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


