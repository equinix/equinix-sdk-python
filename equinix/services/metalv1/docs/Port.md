# Port

Port is a hardware port associated with a reserved or instantiated hardware device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bond** | [**BondPortData**](BondPortData.md) |  | [optional] 
**data** | [**PortData**](PortData.md) |  | [optional] 
**disbond_operation_supported** | **bool** | Indicates whether or not the bond can be broken on the port (when applicable). | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**native_virtual_network** | [**VirtualNetwork**](VirtualNetwork.md) |  | [optional] 
**network_type** | **str** | Composite network type of the bond | [optional] 
**type** | **str** | Type is either \&quot;NetworkBondPort\&quot; for bond ports or \&quot;NetworkPort\&quot; for bondable ethernet ports | [optional] 
**virtual_networks** | [**List[VirtualNetwork]**](VirtualNetwork.md) |  | [optional] 

## Example

```python
from equinix_metal.models.port import Port

# TODO update the JSON string below
json = "{}"
# create an instance of Port from a JSON string
port_instance = Port.from_json(json)
# print the JSON string representation of the object
print(Port.to_json())

# convert the object into a dict
port_dict = port_instance.to_dict()
# create an instance of Port from a dict
port_form_dict = port.from_dict(port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


