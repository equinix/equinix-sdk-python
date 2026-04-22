# CloudRouterRouteFiltersFilter

Top-level filter that can be either an AND expression or OR expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterRouteFilterExpression]**](CloudRouterRouteFilterExpression.md) |  | [optional] 
**var_or** | [**List[CloudRouterRouteFilterExpression]**](CloudRouterRouteFilterExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filters_filter import CloudRouterRouteFiltersFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFiltersFilter from a JSON string
cloud_router_route_filters_filter_instance = CloudRouterRouteFiltersFilter.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFiltersFilter.to_json())

# convert the object into a dict
cloud_router_route_filters_filter_dict = cloud_router_route_filters_filter_instance.to_dict()
# create an instance of CloudRouterRouteFiltersFilter from a dict
cloud_router_route_filters_filter_from_dict = CloudRouterRouteFiltersFilter.from_dict(cloud_router_route_filters_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


