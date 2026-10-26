# TunnelRoutingProtocolIpv4

IPv4 configuration for the Routing Protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable the Routing Protocol on IPv4 | [optional] 
**local_peer_ip** | **str** | The local IP address | [optional] 
**remote_peer_ip** | **str** | The remote peer&#39;s IP address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.tunnel_routing_protocol_ipv4 import TunnelRoutingProtocolIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelRoutingProtocolIpv4 from a JSON string
tunnel_routing_protocol_ipv4_instance = TunnelRoutingProtocolIpv4.from_json(json)
# print the JSON string representation of the object
print(TunnelRoutingProtocolIpv4.to_json())

# convert the object into a dict
tunnel_routing_protocol_ipv4_dict = tunnel_routing_protocol_ipv4_instance.to_dict()
# create an instance of TunnelRoutingProtocolIpv4 from a dict
tunnel_routing_protocol_ipv4_from_dict = TunnelRoutingProtocolIpv4.from_dict(tunnel_routing_protocol_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


