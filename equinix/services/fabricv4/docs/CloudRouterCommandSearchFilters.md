# CloudRouterCommandSearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterCommandSearchFilter]**](CloudRouterCommandSearchFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_command_search_filters import CloudRouterCommandSearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterCommandSearchFilters from a JSON string
cloud_router_command_search_filters_instance = CloudRouterCommandSearchFilters.from_json(json)
# print the JSON string representation of the object
print(CloudRouterCommandSearchFilters.to_json())

# convert the object into a dict
cloud_router_command_search_filters_dict = cloud_router_command_search_filters_instance.to_dict()
# create an instance of CloudRouterCommandSearchFilters from a dict
cloud_router_command_search_filters_from_dict = CloudRouterCommandSearchFilters.from_dict(cloud_router_command_search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


