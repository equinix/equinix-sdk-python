# CloudRouterFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[CloudRouterFilter]**](CloudRouterFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_filters import CloudRouterFilters

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterFilters from a JSON string
cloud_router_filters_instance = CloudRouterFilters.from_json(json)
# print the JSON string representation of the object
print(CloudRouterFilters.to_json())

# convert the object into a dict
cloud_router_filters_dict = cloud_router_filters_instance.to_dict()
# create an instance of CloudRouterFilters from a dict
cloud_router_filters_form_dict = cloud_router_filters.from_dict(cloud_router_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


