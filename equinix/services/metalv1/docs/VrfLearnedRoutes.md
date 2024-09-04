# VrfLearnedRoutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**origin_as** | **int** | The ASN of the peer that advertised the prefix. | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_learned_routes import VrfLearnedRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of VrfLearnedRoutes from a JSON string
vrf_learned_routes_instance = VrfLearnedRoutes.from_json(json)
# print the JSON string representation of the object
print(VrfLearnedRoutes.to_json())

# convert the object into a dict
vrf_learned_routes_dict = vrf_learned_routes_instance.to_dict()
# create an instance of VrfLearnedRoutes from a dict
vrf_learned_routes_form_dict = vrf_learned_routes.from_dict(vrf_learned_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


