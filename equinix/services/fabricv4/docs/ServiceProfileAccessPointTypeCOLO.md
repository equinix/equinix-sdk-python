# ServiceProfileAccessPointTypeCOLO

Colo Access Point Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | [**ServiceProfileAccessPointTypeEnum**](ServiceProfileAccessPointTypeEnum.md) |  | 
**supported_bandwidths** | **List[int]** |  | [optional] 
**allow_remote_connections** | **bool** | Setting to allow or prohibit remote connections to the service profile. | [optional] [default to False]
**allow_custom_bandwidth** | **bool** | Setting to enable or disable the ability of the buyer to customize the bandwidth. | [optional] [default to False]
**bandwidth_alert_threshold** | **float** | percentage of port bandwidth at which an allocation alert is generated - missing on wiki. | [optional] 
**allow_bandwidth_auto_approval** | **bool** | Setting to enable or disable the ability of the buyer to change connection bandwidth without approval of the seller. | [optional] [default to False]
**allow_bandwidth_upgrade** | **bool** | Availability of a bandwidth upgrade. The default is false. | [optional] 
**link_protocol_config** | [**ServiceProfileLinkProtocolConfig**](ServiceProfileLinkProtocolConfig.md) |  | [optional] 
**enable_auto_generate_service_key** | **bool** | for verizon only. | [optional] 
**connection_redundancy_required** | **bool** | Mandate redundant connections | [optional] [default to False]
**api_config** | [**ApiConfig**](ApiConfig.md) |  | [optional] 
**connection_label** | **str** | custom name for \&quot;Connection\&quot; | [optional] 
**authentication_key** | [**AuthenticationKey**](AuthenticationKey.md) |  | [optional] 
**metadata** | [**ServiceProfileMetadata**](ServiceProfileMetadata.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_access_point_type_colo import ServiceProfileAccessPointTypeCOLO

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileAccessPointTypeCOLO from a JSON string
service_profile_access_point_type_colo_instance = ServiceProfileAccessPointTypeCOLO.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileAccessPointTypeCOLO.to_json())

# convert the object into a dict
service_profile_access_point_type_colo_dict = service_profile_access_point_type_colo_instance.to_dict()
# create an instance of ServiceProfileAccessPointTypeCOLO from a dict
service_profile_access_point_type_colo_form_dict = service_profile_access_point_type_colo.from_dict(service_profile_access_point_type_colo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


