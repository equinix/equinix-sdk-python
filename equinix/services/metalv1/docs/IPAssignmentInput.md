# IPAssignmentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**customdata** | **object** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.ip_assignment_input import IPAssignmentInput

# TODO update the JSON string below
json = "{}"
# create an instance of IPAssignmentInput from a JSON string
ip_assignment_input_instance = IPAssignmentInput.from_json(json)
# print the JSON string representation of the object
print(IPAssignmentInput.to_json())

# convert the object into a dict
ip_assignment_input_dict = ip_assignment_input_instance.to_dict()
# create an instance of IPAssignmentInput from a dict
ip_assignment_input_form_dict = ip_assignment_input.from_dict(ip_assignment_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


