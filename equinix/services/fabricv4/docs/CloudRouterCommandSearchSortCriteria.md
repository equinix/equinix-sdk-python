# CloudRouterCommandSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**CloudRouterCommandSearchSortDirection**](CloudRouterCommandSearchSortDirection.md) |  | [optional] [default to CloudRouterCommandSearchSortDirection.DESC]
**var_property** | [**CloudRouterCommandSearchSortBy**](CloudRouterCommandSearchSortBy.md) |  | [optional] [default to CloudRouterCommandSearchSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_search_sort_criteria import CloudRouterCommandSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandSearchSortCriteria from a JSON string
cloud_router_command_search_sort_criteria_instance = CloudRouterCommandSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandSearchSortCriteria.to_json())

# convert the object into a dict
cloud_router_command_search_sort_criteria_dict = cloud_router_command_search_sort_criteria_instance.to_dict()
# create an instance of CloudRouterCommandSearchSortCriteria from a dict
cloud_router_command_search_sort_criteria_from_dict = CloudRouterCommandSearchSortCriteria.from_dict(cloud_router_command_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


