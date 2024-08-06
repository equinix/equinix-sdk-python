# LinkProtocolVxlan

Connection link protocol configuration - VXLAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**vni** | **int** | Virtual Network Identifier | 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_vxlan import LinkProtocolVxlan

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolVxlan from a JSON string
link_protocol_vxlan_instance = LinkProtocolVxlan.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolVxlan.to_json())

# convert the object into a dict
link_protocol_vxlan_dict = link_protocol_vxlan_instance.to_dict()
# create an instance of LinkProtocolVxlan from a dict
link_protocol_vxlan_from_dict = LinkProtocolVxlan.from_dict(link_protocol_vxlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


