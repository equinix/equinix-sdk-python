# CloudRouterOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CloudRouterSimpleExpression]**](CloudRouterSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_or_filter import CloudRouterOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterOrFilter from a JSON string
cloud_router_or_filter_instance = CloudRouterOrFilter.from_json(json)
# print the JSON string representation of the object
print(CloudRouterOrFilter.to_json())

# convert the object into a dict
cloud_router_or_filter_dict = cloud_router_or_filter_instance.to_dict()
# create an instance of CloudRouterOrFilter from a dict
cloud_router_or_filter_form_dict = cloud_router_or_filter.from_dict(cloud_router_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


