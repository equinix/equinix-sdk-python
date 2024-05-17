# PortVlanAssignmentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**vlan_assignments** | [**List[PortVlanAssignment]**](PortVlanAssignment.md) |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment_list import PortVlanAssignmentList

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignmentList from a JSON string
port_vlan_assignment_list_instance = PortVlanAssignmentList.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignmentList.to_json())

# convert the object into a dict
port_vlan_assignment_list_dict = port_vlan_assignment_list_instance.to_dict()
# create an instance of PortVlanAssignmentList from a dict
port_vlan_assignment_list_form_dict = port_vlan_assignment_list.from_dict(port_vlan_assignment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


