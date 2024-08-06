# LinkProtocolEvpnVxlan

Connection link protocol configuration - EVPN_VXLAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**vnid** | **int** | Virtual Network Identifier | 
**type5vni** | **int** | Type 5 VNI identifier | 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_evpn_vxlan import LinkProtocolEvpnVxlan

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolEvpnVxlan from a JSON string
link_protocol_evpn_vxlan_instance = LinkProtocolEvpnVxlan.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolEvpnVxlan.to_json())

# convert the object into a dict
link_protocol_evpn_vxlan_dict = link_protocol_evpn_vxlan_instance.to_dict()
# create an instance of LinkProtocolEvpnVxlan from a dict
link_protocol_evpn_vxlan_from_dict = LinkProtocolEvpnVxlan.from_dict(link_protocol_evpn_vxlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


