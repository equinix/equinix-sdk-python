# VirtualNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_to** | [**Project**](Project.md) |  | [optional] 
**assigned_to_virtual_circuit** | **bool** | True if the virtual network is attached to a virtual circuit. False if not. | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**facility** | [**Href**](Href.md) |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**instances** | [**List[Device]**](Device.md) | A list of instances with ports currently associated to this Virtual Network. | [optional] 
**metal_gateways** | [**List[MetalGatewayLite]**](MetalGatewayLite.md) | A list of metal gateways currently associated to this Virtual Network. | [optional] 
**metro** | [**Metro**](Metro.md) |  | [optional] 
**metro_code** | **str** | The Metro code of the metro in which this Virtual Network is defined. | [optional] 
**tags** | **List[str]** |  | [optional] 
**vxlan** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.virtual_network import VirtualNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNetwork from a JSON string
virtual_network_instance = VirtualNetwork.from_json(json)
# print the JSON string representation of the object
print(VirtualNetwork.to_json())

# convert the object into a dict
virtual_network_dict = virtual_network_instance.to_dict()
# create an instance of VirtualNetwork from a dict
virtual_network_form_dict = virtual_network.from_dict(virtual_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


