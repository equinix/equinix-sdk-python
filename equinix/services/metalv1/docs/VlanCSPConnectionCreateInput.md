# VlanCSPConnectionCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** | The preferred email used for communication and notifications about the Equinix Fabric interconnection. Required when using a Project API key. Optional and defaults to the primary user email address when using a User API key. | [optional] 
**description** | **str** |  | [optional] 
**fabric_provider** | [**VlanCSPConnectionCreateInputFabricProvider**](VlanCSPConnectionCreateInputFabricProvider.md) |  | 
**href** | **str** |  | [optional] 
**metro** | **str** | A Metro ID or code. When creating Fabric VCs (Metal Billed), this is where interconnection will be originating from, as we pre-authorize the use of one of our shared ports as the origin of the interconnection using A-Side service tokens. We only allow local connections for Fabric VCs (Metal Billed), so the destination location must be the same as the origin. For Fabric VCs (Fabric Billed), or shared connections, this will be the destination of the interconnection. We allow remote connections for Fabric VCs (Fabric Billed), so the origin of the interconnection can be a different metro set here. | 
**name** | **str** |  | 
**project** | **str** |  | 
**speed** | **str** | A interconnection speed, in bps, mbps, or gbps. For Fabric VCs, this represents the maximum speed of the interconnection. For Fabric VCs (Metal Billed), this can only be one of the following: &#39;&#39;50mbps&#39;&#39;, &#39;&#39;200mbps&#39;&#39;, &#39;&#39;500mbps&#39;&#39;, &#39;&#39;1gbps&#39;&#39;, &#39;&#39;2gbps&#39;&#39;, &#39;&#39;5gbps&#39;&#39; or &#39;&#39;10gbps&#39;&#39;, and is required for creation. For Fabric VCs (Fabric Billed), this field will always default to &#39;&#39;10gbps&#39;&#39; even if it is not provided. For example, &#39;&#39;500000000&#39;&#39;, &#39;&#39;50m&#39;&#39;, or&#39; &#39;&#39;500mbps&#39;&#39; will all work as valid inputs. | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**vlans** | **List[int]** | A list of one or two metro-based VLANs that will be set on the virtual circuits of primary and/or secondary interconnections respectively when creating Fabric VCs. VLANs can also be set after the interconnection is created, but are required to fully activate the virtual circuits. | 

## Example

```python
from equinix_metal.models.vlan_csp_connection_create_input import VlanCSPConnectionCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VlanCSPConnectionCreateInput from a JSON string
vlan_csp_connection_create_input_instance = VlanCSPConnectionCreateInput.from_json(json)
# print the JSON string representation of the object
print(VlanCSPConnectionCreateInput.to_json())

# convert the object into a dict
vlan_csp_connection_create_input_dict = vlan_csp_connection_create_input_instance.to_dict()
# create an instance of VlanCSPConnectionCreateInput from a dict
vlan_csp_connection_create_input_form_dict = vlan_csp_connection_create_input.from_dict(vlan_csp_connection_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


