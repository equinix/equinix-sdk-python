# ProjectIdName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.project_id_name import ProjectIdName

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectIdName from a JSON string
project_id_name_instance = ProjectIdName.from_json(json)
# print the JSON string representation of the object
print(ProjectIdName.to_json())

# convert the object into a dict
project_id_name_dict = project_id_name_instance.to_dict()
# create an instance of ProjectIdName from a dict
project_id_name_form_dict = project_id_name.from_dict(project_id_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


