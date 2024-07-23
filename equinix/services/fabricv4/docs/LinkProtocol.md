# LinkProtocol

Connection link protocol Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | 
**ipv4** | [**LinkProtocolIpv4Ipv6Config**](LinkProtocolIpv4Ipv6Config.md) |  | [optional] 
**ipv6** | [**LinkProtocolIpv4Ipv6Config**](LinkProtocolIpv4Ipv6Config.md) |  | [optional] 
**tag_protocol_id** | **str** | Tag protocol identifier | [optional] 
**vlan_tag** | **str** | VLAN tag | 
**vlan_tag_min** | **int** | VLAN tag Min value specified for DOT1Q connections | [optional] 
**vlan_tag_max** | **int** | VLAN tag Max value specified for DOT1Q connections | [optional] 
**inner_tag_protocol_id** | **int** | Inner tag protocol identifier | 
**outer_tag_protocol_id** | **int** | Outer tag protocol identifier | 
**vlan_c_tag** | **int** | Inner tag, i.e., C-VLAN tag | 
**vlan_s_tag** | **int** | Outer tag, i.e., S-VLAN tag | 
**vlan_c_tag_min** | **int** | Outer tag Min value specified for QINQ connections | [optional] 
**vlan_c_tag_max** | **int** | Outer tag Max value specified for QINQ connections | [optional] 
**sub_interface** | **int** | Subinterface identifier | [optional] 
**vni** | **int** | Virtual Network Identifier | 
**vnid** | **int** | Virtual Network Identifier | 
**type5vni** | **int** | Type 5 VNI identifier | 

## Example

```python
from equinix.services.fabricv4.models.link_protocol import LinkProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocol from a JSON string
link_protocol_instance = LinkProtocol.from_json(json)
# print the JSON string representation of the object
print(LinkProtocol.to_json())

# convert the object into a dict
link_protocol_dict = link_protocol_instance.to_dict()
# create an instance of LinkProtocol from a dict
link_protocol_form_dict = link_protocol.from_dict(link_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


