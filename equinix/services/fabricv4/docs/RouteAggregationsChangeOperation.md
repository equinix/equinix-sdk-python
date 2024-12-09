# RouteAggregationsChangeOperation

Route Aggregation change operation data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**RoutingProtocolChangeOperationOp**](RoutingProtocolChangeOperationOp.md) |  | 
**path** | **str** | path inside document leading to updated parameter | 
**value** | [**RouteAggregationsBase**](RouteAggregationsBase.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_change_operation import RouteAggregationsChangeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsChangeOperation from a JSON string
route_aggregations_change_operation_instance = RouteAggregationsChangeOperation.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsChangeOperation.to_json())

# convert the object into a dict
route_aggregations_change_operation_dict = route_aggregations_change_operation_instance.to_dict()
# create an instance of RouteAggregationsChangeOperation from a dict
route_aggregations_change_operation_form_dict = route_aggregations_change_operation.from_dict(route_aggregations_change_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


