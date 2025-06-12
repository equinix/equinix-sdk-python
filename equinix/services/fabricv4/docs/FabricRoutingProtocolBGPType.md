# FabricRoutingProtocolBGPType

Defines the structure for BGP routing protocol configuration, including protocol type, BGP IPv4 settings, customer ASN, authentication key, and deployment properties. 

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
from equinix.services.fabricv4.models.fabric_routing_protocol_bgp_type import FabricRoutingProtocolBGPType

# TODO update the JSON string below
json = "{}"
# create an instance of FabricRoutingProtocolBGPType from a JSON string
fabric_routing_protocol_bgp_type_instance = FabricRoutingProtocolBGPType.from_json(json)
# print the JSON string representation of the object
print(FabricRoutingProtocolBGPType.to_json())

# convert the object into a dict
fabric_routing_protocol_bgp_type_dict = fabric_routing_protocol_bgp_type_instance.to_dict()
# create an instance of FabricRoutingProtocolBGPType from a dict
fabric_routing_protocol_bgp_type_from_dict = FabricRoutingProtocolBGPType.from_dict(fabric_routing_protocol_bgp_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


