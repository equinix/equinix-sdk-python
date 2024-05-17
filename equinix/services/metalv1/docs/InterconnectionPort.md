# InterconnectionPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**link_status** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | [**Href**](Href.md) |  | [optional] 
**role** | **str** | Either &#39;primary&#39; or &#39;secondary&#39;. | [optional] 
**speed** | **int** |  | [optional] 
**status** | **str** | For both Fabric VCs and Dedicated Ports, this will be &#39;requested&#39; on creation and &#39;deleting&#39; on deletion. Once the Fabric VC has found its corresponding Fabric connection, this will turn to &#39;active&#39;. For Dedicated Ports, once the dedicated port is associated, this will also turn to &#39;active&#39;. For Fabric VCs, this can turn into an &#39;expired&#39; state if the service token associated is expired. | [optional] 
**switch_id** | **str** | A switch &#39;short ID&#39; | [optional] 
**virtual_circuits** | [**List[VirtualCircuit]**](VirtualCircuit.md) |  | [optional] 

## Example

```python
from equinix_metal.models.interconnection_port import InterconnectionPort

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionPort from a JSON string
interconnection_port_instance = InterconnectionPort.from_json(json)
# print the JSON string representation of the object
print(InterconnectionPort.to_json())

# convert the object into a dict
interconnection_port_dict = interconnection_port_instance.to_dict()
# create an instance of InterconnectionPort from a dict
interconnection_port_form_dict = interconnection_port.from_dict(interconnection_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


