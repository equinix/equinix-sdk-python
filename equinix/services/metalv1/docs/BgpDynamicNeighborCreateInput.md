# BgpDynamicNeighborCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp_neighbor_asn** | **int** | The ASN of the dynamic BGP neighbor | 
**bgp_neighbor_range** | **str** | Network range of the dynamic BGP neighbor in CIDR format | 
**href** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.bgp_dynamic_neighbor_create_input import BgpDynamicNeighborCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of BgpDynamicNeighborCreateInput from a JSON string
bgp_dynamic_neighbor_create_input_instance = BgpDynamicNeighborCreateInput.from_json(json)
# print the JSON string representation of the object
print(BgpDynamicNeighborCreateInput.to_json())

# convert the object into a dict
bgp_dynamic_neighbor_create_input_dict = bgp_dynamic_neighbor_create_input_instance.to_dict()
# create an instance of BgpDynamicNeighborCreateInput from a dict
bgp_dynamic_neighbor_create_input_form_dict = bgp_dynamic_neighbor_create_input.from_dict(bgp_dynamic_neighbor_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


