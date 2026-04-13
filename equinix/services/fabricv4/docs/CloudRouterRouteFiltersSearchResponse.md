# CloudRouterRouteFiltersSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[ConnectionRouteFilterData]**](ConnectionRouteFilterData.md) | List of route filter attachments for a given cloud router | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_route_filters_search_response import CloudRouterRouteFiltersSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterRouteFiltersSearchResponse from a JSON string
cloud_router_route_filters_search_response_instance = CloudRouterRouteFiltersSearchResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterRouteFiltersSearchResponse.to_json())

# convert the object into a dict
cloud_router_route_filters_search_response_dict = cloud_router_route_filters_search_response_instance.to_dict()
# create an instance of CloudRouterRouteFiltersSearchResponse from a dict
cloud_router_route_filters_search_response_from_dict = CloudRouterRouteFiltersSearchResponse.from_dict(cloud_router_route_filters_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


