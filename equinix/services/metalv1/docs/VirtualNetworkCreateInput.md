# VirtualNetworkCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**facility** | **str** | The UUID (or facility code) for the Facility in which to create this Virtual network. | [optional] 
**href** | **str** |  | [optional] 
**metro** | **str** | The UUID (or metro code) for the Metro in which to create this Virtual Network. | [optional] 
**tags** | **List[str]** |  | [optional] 
**vxlan** | **int** | VLAN ID between 2-3999. Must be unique for the project within the Metro in which this Virtual Network is being created. If no value is specified, the next-available VLAN ID in the range 1000-1999 will be automatically selected. | [optional] 

## Example

```python
from equinix_metal.models.virtual_network_create_input import VirtualNetworkCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNetworkCreateInput from a JSON string
virtual_network_create_input_instance = VirtualNetworkCreateInput.from_json(json)
# print the JSON string representation of the object
print(VirtualNetworkCreateInput.to_json())

# convert the object into a dict
virtual_network_create_input_dict = virtual_network_create_input_instance.to_dict()
# create an instance of VirtualNetworkCreateInput from a dict
virtual_network_create_input_form_dict = virtual_network_create_input.from_dict(virtual_network_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


