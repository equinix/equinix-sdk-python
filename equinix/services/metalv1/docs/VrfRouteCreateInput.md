# VrfRouteCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**next_hop** | **str** | The IPv4 address within the VRF of the host that will handle this route | 
**prefix** | **str** | The IPv4 prefix for the route, in CIDR-style notation. For a static default route, this will always be \&quot;0.0.0.0/0\&quot; | 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_route_create_input import VrfRouteCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VrfRouteCreateInput from a JSON string
vrf_route_create_input_instance = VrfRouteCreateInput.from_json(json)
# print the JSON string representation of the object
print(VrfRouteCreateInput.to_json())

# convert the object into a dict
vrf_route_create_input_dict = vrf_route_create_input_instance.to_dict()
# create an instance of VrfRouteCreateInput from a dict
vrf_route_create_input_form_dict = vrf_route_create_input.from_dict(vrf_route_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


