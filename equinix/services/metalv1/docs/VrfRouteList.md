# VrfRouteList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 
**routes** | [**List[VrfRoute]**](VrfRoute.md) |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_route_list import VrfRouteList

# TODO update the JSON string below
json = "{}"
# create an instance of VrfRouteList from a JSON string
vrf_route_list_instance = VrfRouteList.from_json(json)
# print the JSON string representation of the object
print(VrfRouteList.to_json())

# convert the object into a dict
vrf_route_list_dict = vrf_route_list_instance.to_dict()
# create an instance of VrfRouteList from a dict
vrf_route_list_form_dict = vrf_route_list.from_dict(vrf_route_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


