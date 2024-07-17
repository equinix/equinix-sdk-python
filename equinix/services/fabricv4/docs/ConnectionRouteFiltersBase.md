# ConnectionRouteFiltersBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**ConnectionRouteFiltersBaseDirection**](ConnectionRouteFiltersBaseDirection.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.connection_route_filters_base import ConnectionRouteFiltersBase

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRouteFiltersBase from a JSON string
connection_route_filters_base_instance = ConnectionRouteFiltersBase.from_json(json)
# print the JSON string representation of the object
print(ConnectionRouteFiltersBase.to_json())

# convert the object into a dict
connection_route_filters_base_dict = connection_route_filters_base_instance.to_dict()
# create an instance of ConnectionRouteFiltersBase from a dict
connection_route_filters_base_form_dict = connection_route_filters_base.from_dict(connection_route_filters_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


