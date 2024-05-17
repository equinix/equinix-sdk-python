# VrfRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**href** | **str** |  | [optional] [readonly] 
**id** | **str** | The unique identifier for the newly-created resource | [optional] [readonly] 
**metal_gateway** | [**VrfMetalGateway**](VrfMetalGateway.md) |  | [optional] 
**next_hop** | **str** | The next-hop IPv4 address for the route | [optional] 
**prefix** | **str** | The IPv4 prefix for the route, in CIDR-style notation | [optional] 
**status** | **str** | The status of the route. Potential values are \&quot;pending\&quot;, \&quot;active\&quot;, \&quot;deleting\&quot;, and \&quot;error\&quot;, representing various lifecycle states of the route and whether or not it has been successfully configured on the network | [optional] [readonly] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | VRF route type, like &#39;bgp&#39;, &#39;connected&#39;, and &#39;static&#39;. Currently, only static routes are supported | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**vrf** | [**Vrf**](Vrf.md) |  | [optional] 

## Example

```python
from equinix_metal.models.vrf_route import VrfRoute

# TODO update the JSON string below
json = "{}"
# create an instance of VrfRoute from a JSON string
vrf_route_instance = VrfRoute.from_json(json)
# print the JSON string representation of the object
print(VrfRoute.to_json())

# convert the object into a dict
vrf_route_dict = vrf_route_instance.to_dict()
# create an instance of VrfRoute from a dict
vrf_route_form_dict = vrf_route.from_dict(vrf_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


