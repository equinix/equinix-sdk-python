# RouteFiltersDataProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Subscriber-assigned project ID | 
**href** | **str** | Project URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filters_data_project import RouteFiltersDataProject

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersDataProject from a JSON string
route_filters_data_project_instance = RouteFiltersDataProject.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersDataProject.to_json())

# convert the object into a dict
route_filters_data_project_dict = route_filters_data_project_instance.to_dict()
# create an instance of RouteFiltersDataProject from a dict
route_filters_data_project_from_dict = RouteFiltersDataProject.from_dict(route_filters_data_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


