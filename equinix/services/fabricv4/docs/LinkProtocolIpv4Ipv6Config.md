# LinkProtocolIpv4Ipv6Config

IPv4 or IPv6 specific configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_prefix** | **str** | Link subnet prefix | [optional] 
**local_iface_ip** | **str** | Prefix datatype when linkPrefix not specified | [optional] 
**remote_iface_ip** | **str** | Equinix-side link interface address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_ipv4_ipv6_config import LinkProtocolIpv4Ipv6Config

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolIpv4Ipv6Config from a JSON string
link_protocol_ipv4_ipv6_config_instance = LinkProtocolIpv4Ipv6Config.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolIpv4Ipv6Config.to_json())

# convert the object into a dict
link_protocol_ipv4_ipv6_config_dict = link_protocol_ipv4_ipv6_config_instance.to_dict()
# create an instance of LinkProtocolIpv4Ipv6Config from a dict
link_protocol_ipv4_ipv6_config_from_dict = LinkProtocolIpv4Ipv6Config.from_dict(link_protocol_ipv4_ipv6_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


