# ProjectUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_transfer_enabled** | **bool** |  | [optional] 
**customdata** | **object** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** | The name of the project. Cannot contain characters encoded in greater than 3 bytes such as emojis. | [optional] 
**payment_method_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from equinix_metal.models.project_update_input import ProjectUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateInput from a JSON string
project_update_input_instance = ProjectUpdateInput.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateInput.to_json())

# convert the object into a dict
project_update_input_dict = project_update_input_instance.to_dict()
# create an instance of ProjectUpdateInput from a dict
project_update_input_form_dict = project_update_input.from_dict(project_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


