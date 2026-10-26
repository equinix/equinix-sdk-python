# TunnelRoutingProtocolPostRequestIpv4

IPv4 configuration for the Routing Protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable the Routing Protocol on IPv4 | [optional] 

## Example

```python
from equinix.services.fabricv4.models.tunnel_routing_protocol_post_request_ipv4 import TunnelRoutingProtocolPostRequestIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelRoutingProtocolPostRequestIpv4 from a JSON string
tunnel_routing_protocol_post_request_ipv4_instance = TunnelRoutingProtocolPostRequestIpv4.from_json(json)
# print the JSON string representation of the object
print(TunnelRoutingProtocolPostRequestIpv4.to_json())

# convert the object into a dict
tunnel_routing_protocol_post_request_ipv4_dict = tunnel_routing_protocol_post_request_ipv4_instance.to_dict()
# create an instance of TunnelRoutingProtocolPostRequestIpv4 from a dict
tunnel_routing_protocol_post_request_ipv4_from_dict = TunnelRoutingProtocolPostRequestIpv4.from_dict(tunnel_routing_protocol_post_request_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


