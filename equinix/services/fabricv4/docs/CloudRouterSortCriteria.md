# CloudRouterSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**CloudRouterSortDirection**](CloudRouterSortDirection.md) |  | [optional] [default to CloudRouterSortDirection.DESC]
**var_property** | [**CloudRouterSortBy**](CloudRouterSortBy.md) |  | [optional] [default to CloudRouterSortBy.CHANGE_LOG_SLASH_UPDATED_DATE_TIME]

## Example

```python
from equinix.services.fabricv4.models.cloud_router_sort_criteria import CloudRouterSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterSortCriteria from a JSON string
cloud_router_sort_criteria_instance = CloudRouterSortCriteria.from_json(json)
# print the JSON string representation of the object
print(CloudRouterSortCriteria.to_json())

# convert the object into a dict
cloud_router_sort_criteria_dict = cloud_router_sort_criteria_instance.to_dict()
# create an instance of CloudRouterSortCriteria from a dict
cloud_router_sort_criteria_from_dict = CloudRouterSortCriteria.from_dict(cloud_router_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


