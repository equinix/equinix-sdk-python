# VrfLearnedRoutesLearnedRoutesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_as** | **int** | The ASN of the peer that advertised the prefix. | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_learned_routes_learned_routes_inner import VrfLearnedRoutesLearnedRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of VrfLearnedRoutesLearnedRoutesInner from a JSON string
vrf_learned_routes_learned_routes_inner_instance = VrfLearnedRoutesLearnedRoutesInner.from_json(json)
# print the JSON string representation of the object
print(VrfLearnedRoutesLearnedRoutesInner.to_json())

# convert the object into a dict
vrf_learned_routes_learned_routes_inner_dict = vrf_learned_routes_learned_routes_inner_instance.to_dict()
# create an instance of VrfLearnedRoutesLearnedRoutesInner from a dict
vrf_learned_routes_learned_routes_inner_form_dict = vrf_learned_routes_learned_routes_inner.from_dict(vrf_learned_routes_learned_routes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


