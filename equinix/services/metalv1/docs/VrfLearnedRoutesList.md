# VrfLearnedRoutesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**learned_routes** | [**List[VrfLearnedRoutes]**](VrfLearnedRoutes.md) |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_learned_routes_list import VrfLearnedRoutesList

# TODO update the JSON string below
json = "{}"
# create an instance of VrfLearnedRoutesList from a JSON string
vrf_learned_routes_list_instance = VrfLearnedRoutesList.from_json(json)
# print the JSON string representation of the object
print(VrfLearnedRoutesList.to_json())

# convert the object into a dict
vrf_learned_routes_list_dict = vrf_learned_routes_list_instance.to_dict()
# create an instance of VrfLearnedRoutesList from a dict
vrf_learned_routes_list_form_dict = vrf_learned_routes_list.from_dict(vrf_learned_routes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


