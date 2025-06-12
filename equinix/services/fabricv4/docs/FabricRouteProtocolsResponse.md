# FabricRouteProtocolsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Protocol URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned route protocol identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**type** | [**RoutingProtocolBGPTypeType**](RoutingProtocolBGPTypeType.md) |  | 
**name** | **str** |  | [optional] 
**bgp_ipv4** | [**FabricBGPConnectionIpv4**](FabricBGPConnectionIpv4.md) |  | 
**customer_asn** | **int** | Customer asn | 
**bgp_auth_key** | **str** | BGP authorization key | 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_route_protocols_response import FabricRouteProtocolsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricRouteProtocolsResponse from a JSON string
fabric_route_protocols_response_instance = FabricRouteProtocolsResponse.from_json(json)
# print the JSON string representation of the object
print(FabricRouteProtocolsResponse.to_json())

# convert the object into a dict
fabric_route_protocols_response_dict = fabric_route_protocols_response_instance.to_dict()
# create an instance of FabricRouteProtocolsResponse from a dict
fabric_route_protocols_response_from_dict = FabricRouteProtocolsResponse.from_dict(fabric_route_protocols_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


