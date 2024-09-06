# LinkProtocolDot1q

Connection link protocol configuration - DOT1Q

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**tag_protocol_id** | **str** | Tag protocol identifier | [optional] 
**vlan_tag** | **str** | VLAN tag | 
**vlan_tag_min** | **int** | VLAN tag Min value specified for DOT1Q connections | [optional] 
**vlan_tag_max** | **int** | VLAN tag Max value specified for DOT1Q connections | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_dot1q import LinkProtocolDot1q

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolDot1q from a JSON string
link_protocol_dot1q_instance = LinkProtocolDot1q.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolDot1q.to_json())

# convert the object into a dict
link_protocol_dot1q_dict = link_protocol_dot1q_instance.to_dict()
# create an instance of LinkProtocolDot1q from a dict
link_protocol_dot1q_from_dict = LinkProtocolDot1q.from_dict(link_protocol_dot1q_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


