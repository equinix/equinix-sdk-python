# ProcessStep

Definition of customized step while making connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Service profile custom step title | [optional] 
**sub_title** | **str** | Service profile custom step sub title | [optional] 
**description** | **str** | Service profile custom step description | [optional] 

## Example

```python
from equinix.services.fabricv4.models.process_step import ProcessStep

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessStep from a JSON string
process_step_instance = ProcessStep.from_json(json)
# print the JSON string representation of the object
print(ProcessStep.to_json())

# convert the object into a dict
process_step_dict = process_step_instance.to_dict()
# create an instance of ProcessStep from a dict
process_step_from_dict = ProcessStep.from_dict(process_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


