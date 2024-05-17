# PortVlanAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**native** | **bool** |  | [optional] 
**port** | [**Href**](Href.md) |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**virtual_network** | [**Href**](Href.md) |  | [optional] 
**vlan** | **int** |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment import PortVlanAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignment from a JSON string
port_vlan_assignment_instance = PortVlanAssignment.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignment.to_json())

# convert the object into a dict
port_vlan_assignment_dict = port_vlan_assignment_instance.to_dict()
# create an instance of PortVlanAssignment from a dict
port_vlan_assignment_form_dict = port_vlan_assignment.from_dict(port_vlan_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


