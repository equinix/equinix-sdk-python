# BgpSessionNeighbors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_neighbors** | [**List[BgpNeighborData]**](BgpNeighborData.md) | A list of BGP session neighbor data | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_session_neighbors import BgpSessionNeighbors

# TODO update the JSON string below
json = "{}"
# create an instance of BgpSessionNeighbors from a JSON string
bgp_session_neighbors_instance = BgpSessionNeighbors.from_json(json)
# print the JSON string representation of the object
print(BgpSessionNeighbors.to_json())

# convert the object into a dict
bgp_session_neighbors_dict = bgp_session_neighbors_instance.to_dict()
# create an instance of BgpSessionNeighbors from a dict
bgp_session_neighbors_form_dict = bgp_session_neighbors.from_dict(bgp_session_neighbors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


