# LinkProtocolQinq

Connection link protocol configuration - QINQ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**inner_tag_protocol_id** | **int** | Inner tag protocol identifier | 
**outer_tag_protocol_id** | **int** | Outer tag protocol identifier | 
**vlan_c_tag** | **int** | Inner tag, i.e., C-VLAN tag | 
**vlan_s_tag** | **int** | Outer tag, i.e., S-VLAN tag | 
**vlan_c_tag_min** | **int** | Outer tag Min value specified for QINQ connections | [optional] 
**vlan_c_tag_max** | **int** | Outer tag Max value specified for QINQ connections | [optional] 
**sub_interface** | **int** | Subinterface identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_qinq import LinkProtocolQinq

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolQinq from a JSON string
link_protocol_qinq_instance = LinkProtocolQinq.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolQinq.to_json())

# convert the object into a dict
link_protocol_qinq_dict = link_protocol_qinq_instance.to_dict()
# create an instance of LinkProtocolQinq from a dict
link_protocol_qinq_form_dict = link_protocol_qinq.from_dict(link_protocol_qinq_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


