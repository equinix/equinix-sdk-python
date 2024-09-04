# VirtualNetworkUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.virtual_network_update_input import VirtualNetworkUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNetworkUpdateInput from a JSON string
virtual_network_update_input_instance = VirtualNetworkUpdateInput.from_json(json)
# print the JSON string representation of the object
print(VirtualNetworkUpdateInput.to_json())

# convert the object into a dict
virtual_network_update_input_dict = virtual_network_update_input_instance.to_dict()
# create an instance of VirtualNetworkUpdateInput from a dict
virtual_network_update_input_form_dict = virtual_network_update_input.from_dict(virtual_network_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


