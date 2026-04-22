# CloudRouterRouteFiltersSearchBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudRouterRouteFiltersFilter**](CloudRouterRouteFiltersFilter.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[RfAttachmentSortItem]**](RfAttachmentSortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filters_search_base import CloudRouterRouteFiltersSearchBase

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFiltersSearchBase from a JSON string
cloud_router_route_filters_search_base_instance = CloudRouterRouteFiltersSearchBase.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFiltersSearchBase.to_json())

# convert the object into a dict
cloud_router_route_filters_search_base_dict = cloud_router_route_filters_search_base_instance.to_dict()
# create an instance of CloudRouterRouteFiltersSearchBase from a dict
cloud_router_route_filters_search_base_from_dict = CloudRouterRouteFiltersSearchBase.from_dict(cloud_router_route_filters_search_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


