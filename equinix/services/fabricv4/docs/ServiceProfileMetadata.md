# ServiceProfileMetadata

Metadata. Response attribute. Ignored on request payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**props** | **str** |  | [optional] 
**reg_ex** | **str** |  | [optional] 
**reg_ex_msg** | **str** |  | [optional] 
**vlan_range_max_value** | **int** |  | [optional] 
**vlan_range_min_value** | **int** |  | [optional] 
**max_qinq** | **str** |  | [optional] 
**max_dot1q** | **int** |  | [optional] 
**variable_billing** | **bool** |  | [optional] 
**global_organization** | **str** |  | [optional] 
**limit_auth_key_conn** | **bool** |  | [optional] 
**allow_secondary_location** | **bool** |  | [optional] 
**redundant_profile_id** | **str** |  | [optional] 
**allow_vc_migration** | **bool** |  | [optional] 
**connection_editable** | **bool** |  | [optional] 
**release_vlan** | **bool** |  | [optional] 
**max_connections_on_port** | **int** |  | [optional] 
**port_assignment_strategy** | **str** |  | [optional] 
**eqx_managed_port** | **bool** |  | [optional] 
**connection_name_editable** | **bool** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_profile_metadata import ServiceProfileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfileMetadata from a JSON string
service_profile_metadata_instance = ServiceProfileMetadata.from_json(json)
# print the JSON string representation of the object
print(ServiceProfileMetadata.to_json())

# convert the object into a dict
service_profile_metadata_dict = service_profile_metadata_instance.to_dict()
# create an instance of ServiceProfileMetadata from a dict
service_profile_metadata_from_dict = ServiceProfileMetadata.from_dict(service_profile_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


