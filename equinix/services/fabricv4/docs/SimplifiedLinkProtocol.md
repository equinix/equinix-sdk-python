# SimplifiedLinkProtocol

Connection link protocol Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**vlan_tag** | **int** | vlanTag value specified for DOT1Q connections | [optional] 
**vlan_s_tag** | **int** | vlanSTag value specified for QINQ connections | [optional] 
**vlan_c_tag** | **int** | vlanCTag value specified for QINQ connections | [optional] 

## Example

```python
from equinix.services.fabricv4.models.simplified_link_protocol import SimplifiedLinkProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedLinkProtocol from a JSON string
simplified_link_protocol_instance = SimplifiedLinkProtocol.from_json(json)
# print the JSON string representation of the object
print(SimplifiedLinkProtocol.to_json())

# convert the object into a dict
simplified_link_protocol_dict = simplified_link_protocol_instance.to_dict()
# create an instance of SimplifiedLinkProtocol from a dict
simplified_link_protocol_from_dict = SimplifiedLinkProtocol.from_dict(simplified_link_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


