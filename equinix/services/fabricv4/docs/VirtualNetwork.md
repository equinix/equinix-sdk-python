# VirtualNetwork

Virtual Network Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The Canonical URL at which the resource resides. | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned Virtual Network identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.virtual_network import VirtualNetwork

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


