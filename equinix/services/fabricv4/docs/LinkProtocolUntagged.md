# LinkProtocolUntagged

Connection link protocol configuration - UNTAGGED

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LinkProtocolType**](LinkProtocolType.md) |  | [optional] 
**ipv4** | [**LinkProtocolIpv4Ipv6Config**](LinkProtocolIpv4Ipv6Config.md) |  | [optional] 
**ipv6** | [**LinkProtocolIpv4Ipv6Config**](LinkProtocolIpv4Ipv6Config.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_untagged import LinkProtocolUntagged

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolUntagged from a JSON string
link_protocol_untagged_instance = LinkProtocolUntagged.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolUntagged.to_json())

# convert the object into a dict
link_protocol_untagged_dict = link_protocol_untagged_instance.to_dict()
# create an instance of LinkProtocolUntagged from a dict
link_protocol_untagged_form_dict = link_protocol_untagged.from_dict(link_protocol_untagged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


