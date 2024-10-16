# CloudRouterActionsSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterActionsSearchFilter]**](CloudRouterActionsSearchFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_filters import CloudRouterActionsSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchFilters from a JSON string
cloud_router_actions_search_filters_instance = CloudRouterActionsSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchFilters.to_json())

# convert the object into a dict
cloud_router_actions_search_filters_dict = cloud_router_actions_search_filters_instance.to_dict()
# create an instance of CloudRouterActionsSearchFilters from a dict
cloud_router_actions_search_filters_form_dict = cloud_router_actions_search_filters.from_dict(cloud_router_actions_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


