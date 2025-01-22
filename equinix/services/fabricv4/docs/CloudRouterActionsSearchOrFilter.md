# CloudRouterActionsSearchOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CloudRouterActionsSearchExpression]**](CloudRouterActionsSearchExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_actions_search_or_filter import CloudRouterActionsSearchOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterActionsSearchOrFilter from a JSON string
cloud_router_actions_search_or_filter_instance = CloudRouterActionsSearchOrFilter.from_json(json)
# print the JSON string representation of the object
print(CloudRouterActionsSearchOrFilter.to_json())

# convert the object into a dict
cloud_router_actions_search_or_filter_dict = cloud_router_actions_search_or_filter_instance.to_dict()
# create an instance of CloudRouterActionsSearchOrFilter from a dict
cloud_router_actions_search_or_filter_from_dict = CloudRouterActionsSearchOrFilter.from_dict(cloud_router_actions_search_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


