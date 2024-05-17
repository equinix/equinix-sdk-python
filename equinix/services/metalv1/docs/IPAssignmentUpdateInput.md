# IPAssignmentUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customdata** | **object** |  | [optional] 
**details** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.ip_assignment_update_input import IPAssignmentUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of IPAssignmentUpdateInput from a JSON string
ip_assignment_update_input_instance = IPAssignmentUpdateInput.from_json(json)
# print the JSON string representation of the object
print(IPAssignmentUpdateInput.to_json())

# convert the object into a dict
ip_assignment_update_input_dict = ip_assignment_update_input_instance.to_dict()
# create an instance of IPAssignmentUpdateInput from a dict
ip_assignment_update_input_form_dict = ip_assignment_update_input.from_dict(ip_assignment_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


