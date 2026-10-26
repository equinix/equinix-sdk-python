# CrossConnectProject

Cross Connect Project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Project Identifier. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_project import CrossConnectProject

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectProject from a JSON string
cross_connect_project_instance = CrossConnectProject.from_json(json)
# print the JSON string representation of the object
print(CrossConnectProject.to_json())

# convert the object into a dict
cross_connect_project_dict = cross_connect_project_instance.to_dict()
# create an instance of CrossConnectProject from a dict
cross_connect_project_from_dict = CrossConnectProject.from_dict(cross_connect_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


