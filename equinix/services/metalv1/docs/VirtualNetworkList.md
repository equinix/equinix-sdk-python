# VirtualNetworkList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**virtual_networks** | [**List[VirtualNetwork]**](VirtualNetwork.md) |  | [optional] 

## Example

```python
from equinix_metal.models.virtual_network_list import VirtualNetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNetworkList from a JSON string
virtual_network_list_instance = VirtualNetworkList.from_json(json)
# print the JSON string representation of the object
print(VirtualNetworkList.to_json())

# convert the object into a dict
virtual_network_list_dict = virtual_network_list_instance.to_dict()
# create an instance of VirtualNetworkList from a dict
virtual_network_list_form_dict = virtual_network_list.from_dict(virtual_network_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


