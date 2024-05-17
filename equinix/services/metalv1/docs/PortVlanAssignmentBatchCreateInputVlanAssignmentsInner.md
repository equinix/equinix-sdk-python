# PortVlanAssignmentBatchCreateInputVlanAssignmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**native** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**vlan** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment_batch_create_input_vlan_assignments_inner import PortVlanAssignmentBatchCreateInputVlanAssignmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignmentBatchCreateInputVlanAssignmentsInner from a JSON string
port_vlan_assignment_batch_create_input_vlan_assignments_inner_instance = PortVlanAssignmentBatchCreateInputVlanAssignmentsInner.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignmentBatchCreateInputVlanAssignmentsInner.to_json())

# convert the object into a dict
port_vlan_assignment_batch_create_input_vlan_assignments_inner_dict = port_vlan_assignment_batch_create_input_vlan_assignments_inner_instance.to_dict()
# create an instance of PortVlanAssignmentBatchCreateInputVlanAssignmentsInner from a dict
port_vlan_assignment_batch_create_input_vlan_assignments_inner_form_dict = port_vlan_assignment_batch_create_input_vlan_assignments_inner.from_dict(port_vlan_assignment_batch_create_input_vlan_assignments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


