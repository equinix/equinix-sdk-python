# VirtualCircuitList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**virtual_circuits** | [**List[VirtualCircuit]**](VirtualCircuit.md) |  | [optional] 

## Example

```python
from equinix_metal.models.virtual_circuit_list import VirtualCircuitList

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCircuitList from a JSON string
virtual_circuit_list_instance = VirtualCircuitList.from_json(json)
# print the JSON string representation of the object
print(VirtualCircuitList.to_json())

# convert the object into a dict
virtual_circuit_list_dict = virtual_circuit_list_instance.to_dict()
# create an instance of VirtualCircuitList from a dict
virtual_circuit_list_form_dict = virtual_circuit_list.from_dict(virtual_circuit_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


