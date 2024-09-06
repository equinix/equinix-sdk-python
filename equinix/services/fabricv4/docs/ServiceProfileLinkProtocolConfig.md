# ServiceProfileLinkProtocolConfig

Configuration for dot1q to qinq translation support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encapsulation_strategy** | [**ServiceProfileLinkProtocolConfigEncapsulationStrategy**](ServiceProfileLinkProtocolConfigEncapsulationStrategy.md) |  | [optional] 
**named_tags** | **List[str]** |  | [optional] 
**vlan_c_tag_label** | **str** | was ctagLabel | [optional] 
**reuse_vlan_s_tag** | **bool** |  | [optional] [default to False]
**encapsulation** | [**ServiceProfileLinkProtocolConfigEncapsulation**](ServiceProfileLinkProtocolConfigEncapsulation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_link_protocol_config import ServiceProfileLinkProtocolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileLinkProtocolConfig from a JSON string
service_profile_link_protocol_config_instance = ServiceProfileLinkProtocolConfig.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileLinkProtocolConfig.to_json())

# convert the object into a dict
service_profile_link_protocol_config_dict = service_profile_link_protocol_config_instance.to_dict()
# create an instance of ServiceProfileLinkProtocolConfig from a dict
service_profile_link_protocol_config_from_dict = ServiceProfileLinkProtocolConfig.from_dict(service_profile_link_protocol_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


