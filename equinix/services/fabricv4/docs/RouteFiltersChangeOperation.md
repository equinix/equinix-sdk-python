# RouteFiltersChangeOperation

Route filter change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**RoutingProtocolChangeOperationOp**](RoutingProtocolChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | [**RouteFiltersBase**](RouteFiltersBase.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.route_filters_change_operation import RouteFiltersChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFiltersChangeOperation from a JSON string
route_filters_change_operation_instance = RouteFiltersChangeOperation.from_json(json)
# print the JSON string representation of the object
print(RouteFiltersChangeOperation.to_json())

# convert the object into a dict
route_filters_change_operation_dict = route_filters_change_operation_instance.to_dict()
# create an instance of RouteFiltersChangeOperation from a dict
route_filters_change_operation_form_dict = route_filters_change_operation.from_dict(route_filters_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


