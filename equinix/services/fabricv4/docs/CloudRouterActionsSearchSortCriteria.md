# CloudRouterActionsSearchSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**CloudRouterActionsSearchSortDirection**](CloudRouterActionsSearchSortDirection.md) |  | [optional] 
**var_property** | [**CloudRouterActionsSearchSortBy**](CloudRouterActionsSearchSortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_sort_criteria import CloudRouterActionsSearchSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchSortCriteria from a JSON string
cloud_router_actions_search_sort_criteria_instance = CloudRouterActionsSearchSortCriteria.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchSortCriteria.to_json())

# convert the object into a dict
cloud_router_actions_search_sort_criteria_dict = cloud_router_actions_search_sort_criteria_instance.to_dict()
# create an instance of CloudRouterActionsSearchSortCriteria from a dict
cloud_router_actions_search_sort_criteria_form_dict = cloud_router_actions_search_sort_criteria.from_dict(cloud_router_actions_search_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


