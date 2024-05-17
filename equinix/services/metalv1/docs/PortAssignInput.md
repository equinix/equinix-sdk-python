# PortAssignInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**vnid** | **str** | Virtual Network ID. May be the UUID of the Virtual Network record, or the VLAN value itself.  | [optional] 

## Example

```python
from equinix_metal.models.port_assign_input import PortAssignInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortAssignInput from a JSON string
port_assign_input_instance = PortAssignInput.from_json(json)
# print the JSON string representation of the object
print(PortAssignInput.to_json())

# convert the object into a dict
port_assign_input_dict = port_assign_input_instance.to_dict()
# create an instance of PortAssignInput from a dict
port_assign_input_form_dict = port_assign_input.from_dict(port_assign_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


