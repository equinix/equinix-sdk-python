# DedicatedPortCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_account_name** | **str** | The billing account name of the Equinix Fabric account. | [optional] 
**contact_email** | **str** | The preferred email used for communication and notifications about the Equinix Fabric interconnection. Optional and defaults to the primary user email address when using a User API key or the organization owner email address when using a Project API key. | [optional] 
**description** | **str** |  | [optional] 
**facility_id** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | A Metro ID or code. For interconnections with Dedicated Ports, this will be the location of the issued Dedicated Ports. | 
**mode** | **str** | The mode of the interconnection (only relevant to Dedicated Ports). Fabric VCs won&#39;t have this field. Can be either &#39;standard&#39; or &#39;tunnel&#39;.   The default mode of an interconnection on a Dedicated Port is &#39;standard&#39;. The mode can only be changed when there are no associated virtual circuits on the interconnection.   In tunnel mode, an 802.1q tunnel is added to a port to send/receive double tagged packets from server instances. | [optional] 
**name** | **str** |  | 
**project** | **str** |  | [optional] 
**redundancy** | **str** | Either &#39;primary&#39; or &#39;redundant&#39;. | 
**speed** | **str** | A interconnection speed, in bps, mbps, or gbps. For Dedicated Ports, this can be 10Gbps or 100Gbps. | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | When requesting for a dedicated port, the value of this field should be &#39;dedicated&#39;. | 
**use_case** | **str** | The intended use case of the dedicated port. | [optional] 

## Example

```python
from equinix_metal.models.dedicated_port_create_input import DedicatedPortCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedPortCreateInput from a JSON string
dedicated_port_create_input_instance = DedicatedPortCreateInput.from_json(json)
# print the JSON string representation of the object
print(DedicatedPortCreateInput.to_json())

# convert the object into a dict
dedicated_port_create_input_dict = dedicated_port_create_input_instance.to_dict()
# create an instance of DedicatedPortCreateInput from a dict
dedicated_port_create_input_form_dict = dedicated_port_create_input.from_dict(dedicated_port_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


