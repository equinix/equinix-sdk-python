# PortVlanAssignmentBatchCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**vlan_assignments** | [**List[PortVlanAssignmentBatchCreateInputVlanAssignmentsInner]**](PortVlanAssignmentBatchCreateInputVlanAssignmentsInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment_batch_create_input import PortVlanAssignmentBatchCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignmentBatchCreateInput from a JSON string
port_vlan_assignment_batch_create_input_instance = PortVlanAssignmentBatchCreateInput.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignmentBatchCreateInput.to_json())

# convert the object into a dict
port_vlan_assignment_batch_create_input_dict = port_vlan_assignment_batch_create_input_instance.to_dict()
# create an instance of PortVlanAssignmentBatchCreateInput from a dict
port_vlan_assignment_batch_create_input_form_dict = port_vlan_assignment_batch_create_input.from_dict(port_vlan_assignment_batch_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


