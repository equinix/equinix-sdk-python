# PortVlanAssignmentBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**port** | [**Port**](Port.md) |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**vlan_assignments** | [**List[PortVlanAssignmentBatchVlanAssignmentsInner]**](PortVlanAssignmentBatchVlanAssignmentsInner.md) |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment_batch import PortVlanAssignmentBatch

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignmentBatch from a JSON string
port_vlan_assignment_batch_instance = PortVlanAssignmentBatch.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignmentBatch.to_json())

# convert the object into a dict
port_vlan_assignment_batch_dict = port_vlan_assignment_batch_instance.to_dict()
# create an instance of PortVlanAssignmentBatch from a dict
port_vlan_assignment_batch_form_dict = port_vlan_assignment_batch.from_dict(port_vlan_assignment_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


