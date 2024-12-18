# RouteAggregationsChange

Current state of latest Route Aggregation change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteAggregationsChangeType**](RouteAggregationsChangeType.md) |  | 
**href** | **str** | Route AGGREGATION Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_change import RouteAggregationsChange

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsChange from a JSON string
route_aggregations_change_instance = RouteAggregationsChange.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsChange.to_json())

# convert the object into a dict
route_aggregations_change_dict = route_aggregations_change_instance.to_dict()
# create an instance of RouteAggregationsChange from a dict
route_aggregations_change_form_dict = route_aggregations_change.from_dict(route_aggregations_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


