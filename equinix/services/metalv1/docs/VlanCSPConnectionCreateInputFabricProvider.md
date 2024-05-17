# VlanCSPConnectionCreateInputFabricProvider

Configuration information for connecting to external cloud service provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AWS Account ID | 
**href** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from equinix_metal.models.vlan_csp_connection_create_input_fabric_provider import VlanCSPConnectionCreateInputFabricProvider

# TODO update the JSON string below
json = "{}"
# create an instance of VlanCSPConnectionCreateInputFabricProvider from a JSON string
vlan_csp_connection_create_input_fabric_provider_instance = VlanCSPConnectionCreateInputFabricProvider.from_json(json)
# print the JSON string representation of the object
print(VlanCSPConnectionCreateInputFabricProvider.to_json())

# convert the object into a dict
vlan_csp_connection_create_input_fabric_provider_dict = vlan_csp_connection_create_input_fabric_provider_instance.to_dict()
# create an instance of VlanCSPConnectionCreateInputFabricProvider from a dict
vlan_csp_connection_create_input_fabric_provider_form_dict = vlan_csp_connection_create_input_fabric_provider.from_dict(vlan_csp_connection_create_input_fabric_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


