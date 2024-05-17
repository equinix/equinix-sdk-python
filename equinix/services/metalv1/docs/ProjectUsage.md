# ProjectUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**plan** | **str** |  | [optional] 
**plan_version** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.project_usage import ProjectUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUsage from a JSON string
project_usage_instance = ProjectUsage.from_json(json)
# print the JSON string representation of the object
print(ProjectUsage.to_json())

# convert the object into a dict
project_usage_dict = project_usage_instance.to_dict()
# create an instance of ProjectUsage from a dict
project_usage_form_dict = project_usage.from_dict(project_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


