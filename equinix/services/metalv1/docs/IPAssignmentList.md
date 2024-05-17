# IPAssignmentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**ip_addresses** | [**List[IPAssignment]**](IPAssignment.md) |  | [optional] 

## Example

```python
from equinix_metal.models.ip_assignment_list import IPAssignmentList

# TODO update the JSON string below
json = "{}"
# create an instance of IPAssignmentList from a JSON string
ip_assignment_list_instance = IPAssignmentList.from_json(json)
# print the JSON string representation of the object
print(IPAssignmentList.to_json())

# convert the object into a dict
ip_assignment_list_dict = ip_assignment_list_instance.to_dict()
# create an instance of IPAssignmentList from a dict
ip_assignment_list_form_dict = ip_assignment_list.from_dict(ip_assignment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


