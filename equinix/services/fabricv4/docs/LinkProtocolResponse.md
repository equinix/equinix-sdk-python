# LinkProtocolResponse

Link Protocol response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | LinkProtocol URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned network identifier | [optional] 
**state** | [**LinkProtocolState**](LinkProtocolState.md) |  | [optional] 
**type** | [**LinkProtocolRequestType**](LinkProtocolRequestType.md) |  | [optional] 
**vlan_tag** | **int** |  | [optional] 
**vni** | **int** |  | [optional] 
**vlan_tag_min** | **int** |  | [optional] 
**vlan_tag_max** | **int** |  | [optional] 
**vlan_s_tag** | **int** |  | [optional] 
**vlan_c_tag** | **int** |  | [optional] 
**vlan_c_tag_min** | **int** |  | [optional] 
**vlan_c_tag_max** | **int** |  | [optional] 
**sub_interface** | [**SubInterface**](SubInterface.md) |  | [optional] 
**asset** | [**LinkProtocolConnection**](LinkProtocolConnection.md) |  | [optional] 
**service_token** | [**LinkProtocolServiceToken**](LinkProtocolServiceToken.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.link_protocol_response import LinkProtocolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkProtocolResponse from a JSON string
link_protocol_response_instance = LinkProtocolResponse.from_json(json)
# print the JSON string representation of the object
print(LinkProtocolResponse.to_json())

# convert the object into a dict
link_protocol_response_dict = link_protocol_response_instance.to_dict()
# create an instance of LinkProtocolResponse from a dict
link_protocol_response_from_dict = LinkProtocolResponse.from_dict(link_protocol_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


