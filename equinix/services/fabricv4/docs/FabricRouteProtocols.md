# FabricRouteProtocols

The RouteProtocols schema specifies the supported routing protocols for orchestrator providers. It defines the structure and configuration options for each protocol type. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoutingProtocolBGPTypeType**](RoutingProtocolBGPTypeType.md) |  | 
**name** | **str** |  | [optional] 
**uuid** | **str** | Equinix-assigned route protocol identifier | [optional] 
**bgp_ipv4** | [**FabricBGPConnectionIpv4**](FabricBGPConnectionIpv4.md) |  | 
**customer_asn** | **int** | Customer asn | 
**bgp_auth_key** | **str** | BGP authorization key | 
**as_override_enabled** | **bool** | Enable AS number override | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_route_protocols import FabricRouteProtocols

# TODO update the JSON string below
json = "{}"
# create an instance of FabricRouteProtocols from a JSON string
fabric_route_protocols_instance = FabricRouteProtocols.from_json(json)
# print the JSON string representation of the object
print(FabricRouteProtocols.to_json())

# convert the object into a dict
fabric_route_protocols_dict = fabric_route_protocols_instance.to_dict()
# create an instance of FabricRouteProtocols from a dict
fabric_route_protocols_from_dict = FabricRouteProtocols.from_dict(fabric_route_protocols_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


