# PortVlanAssignmentBatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[PortVlanAssignmentBatch]**](PortVlanAssignmentBatch.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.port_vlan_assignment_batch_list import PortVlanAssignmentBatchList

# TODO update the JSON string below
json = "{}"
# create an instance of PortVlanAssignmentBatchList from a JSON string
port_vlan_assignment_batch_list_instance = PortVlanAssignmentBatchList.from_json(json)
# print the JSON string representation of the object
print(PortVlanAssignmentBatchList.to_json())

# convert the object into a dict
port_vlan_assignment_batch_list_dict = port_vlan_assignment_batch_list_instance.to_dict()
# create an instance of PortVlanAssignmentBatchList from a dict
port_vlan_assignment_batch_list_form_dict = port_vlan_assignment_batch_list.from_dict(port_vlan_assignment_batch_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


