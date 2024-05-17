# ProjectUsageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**usages** | [**List[ProjectUsage]**](ProjectUsage.md) |  | [optional] 

## Example

```python
from equinix_metal.models.project_usage_list import ProjectUsageList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUsageList from a JSON string
project_usage_list_instance = ProjectUsageList.from_json(json)
# print the JSON string representation of the object
print(ProjectUsageList.to_json())

# convert the object into a dict
project_usage_list_dict = project_usage_list_instance.to_dict()
# create an instance of ProjectUsageList from a dict
project_usage_list_form_dict = project_usage_list.from_dict(project_usage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


