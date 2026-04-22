# CloudRouterRouteAggregationsSearchBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**CloudRouterRouteAggregationsFilter**](CloudRouterRouteAggregationsFilter.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**sort** | [**List[RaAttachmentSortItem]**](RaAttachmentSortItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_aggregations_search_base import CloudRouterRouteAggregationsSearchBase

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteAggregationsSearchBase from a JSON string
cloud_router_route_aggregations_search_base_instance = CloudRouterRouteAggregationsSearchBase.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteAggregationsSearchBase.to_json())

# convert the object into a dict
cloud_router_route_aggregations_search_base_dict = cloud_router_route_aggregations_search_base_instance.to_dict()
# create an instance of CloudRouterRouteAggregationsSearchBase from a dict
cloud_router_route_aggregations_search_base_from_dict = CloudRouterRouteAggregationsSearchBase.from_dict(cloud_router_route_aggregations_search_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


