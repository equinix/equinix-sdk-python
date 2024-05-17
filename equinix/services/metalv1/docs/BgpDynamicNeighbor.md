# BgpDynamicNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_neighbor_asn** | **int** | The ASN of the dynamic BGP neighbor | [optional] 
**bgp_neighbor_range** | **str** | Network range of the dynamic BGP neighbor in CIDR format | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**created_by** | [**UserLimited**](UserLimited.md) |  | [optional] 
**href** | **str** |  | [optional] [readonly] 
**id** | **str** | The unique identifier for the resource | [optional] [readonly] 
**metal_gateway** | [**VrfMetalGateway**](VrfMetalGateway.md) |  | [optional] 
**state** | **str** |  | [optional] [readonly] 
**tags** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from equinix_metal.models.bgp_dynamic_neighbor import BgpDynamicNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of BgpDynamicNeighbor from a JSON string
bgp_dynamic_neighbor_instance = BgpDynamicNeighbor.from_json(json)
# print the JSON string representation of the object
print(BgpDynamicNeighbor.to_json())

# convert the object into a dict
bgp_dynamic_neighbor_dict = bgp_dynamic_neighbor_instance.to_dict()
# create an instance of BgpDynamicNeighbor from a dict
bgp_dynamic_neighbor_form_dict = bgp_dynamic_neighbor.from_dict(bgp_dynamic_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


