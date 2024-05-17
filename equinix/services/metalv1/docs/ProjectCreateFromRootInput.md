# ProjectCreateFromRootInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customdata** | **object** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** | The name of the project. Cannot contain characters encoded in greater than 3 bytes such as emojis. | 
**organization_id** | **str** |  | [optional] 
**payment_method_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | The type of the project. If no type is specified the project type will automatically be &#x60;default&#x60; Projects of type &#39;vmce&#39; are part of an in development feature and not available to all customers. | [optional] 

## Example

```python
from equinix_metal.models.project_create_from_root_input import ProjectCreateFromRootInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateFromRootInput from a JSON string
project_create_from_root_input_instance = ProjectCreateFromRootInput.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateFromRootInput.to_json())

# convert the object into a dict
project_create_from_root_input_dict = project_create_from_root_input_instance.to_dict()
# create an instance of ProjectCreateFromRootInput from a dict
project_create_from_root_input_form_dict = project_create_from_root_input.from_dict(project_create_from_root_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


