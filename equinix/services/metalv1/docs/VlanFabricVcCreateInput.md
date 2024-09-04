# VlanFabricVcCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** | The preferred email used for communication and notifications about the Equinix Fabric interconnection. Optional and defaults to the primary user email address when using a User API key or the organization owner email address when using a Project API key. | [optional] 
**description** | **str** |  | [optional] 
**facility_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | A Metro ID or code. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here. | 
**name** | **str** |  | 
**project** | **str** |  | [optional] 
**redundancy** | **str** | Either &#39;primary&#39; or &#39;redundant&#39;. | 
**service_token_type** | **str** | Either &#39;a_side&#39; or &#39;z_side&#39;. Setting this field to &#39;a_side&#39; will create an interconnection with Fabric VCs (Metal Billed). Setting this field to &#39;z_side&#39; will create an interconnection with Fabric VCs (Fabric Billed). This is required when the &#39;type&#39; is &#39;shared&#39;, but this is not applicable when the &#39;type&#39; is &#39;dedicated&#39;. This parameter is included in the specification as a developer preview and is generally unavailable. Please contact our Support team for more details. | 
**speed** | **str** | A interconnection speed, in bps, mbps, or gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following:  &#39;&#39;50mbps&#39;&#39;, &#39;&#39;200mbps&#39;&#39;, &#39;&#39;500mbps&#39;&#39;, &#39;&#39;1gbps&#39;&#39;, &#39;&#39;2gbps&#39;&#39;, &#39;&#39;5gbps&#39;&#39; or &#39;&#39;10gbps&#39;&#39;, and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to &#39;&#39;10gbps&#39;&#39; even if it is not provided. For example, &#39;&#39;500000000&#39;&#39;, &#39;&#39;50m&#39;&#39;, or&#39; &#39;&#39;500mbps&#39;&#39; will all work as valid inputs. | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | When requesting for a Fabric VC, the value of this field should be &#39;shared&#39;. | 
**vlans** | **List[int]** | A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary (if redundant) interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the virtual circuits. | 

## Example

```python
from equinix_metal.models.vlan_fabric_vc_create_input import VlanFabricVcCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VlanFabricVcCreateInput from a JSON string
vlan_fabric_vc_create_input_instance = VlanFabricVcCreateInput.from_json(json)
# print the JSON string representation of the object
print(VlanFabricVcCreateInput.to_json())

# convert the object into a dict
vlan_fabric_vc_create_input_dict = vlan_fabric_vc_create_input_instance.to_dict()
# create an instance of VlanFabricVcCreateInput from a dict
vlan_fabric_vc_create_input_form_dict = vlan_fabric_vc_create_input.from_dict(vlan_fabric_vc_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


