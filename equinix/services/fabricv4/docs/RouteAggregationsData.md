# RouteAggregationsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Route Aggregation URI | [optional] 
**type** | [**RouteAggregationsBaseType**](RouteAggregationsBaseType.md) |  | [optional] 
**uuid** | **str** | Route Aggregation identifier | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | Customer-provided connection description | [optional] 
**state** | [**RouteAggregationState**](RouteAggregationState.md) |  | [optional] 
**change** | [**RouteAggregationsChange**](RouteAggregationsChange.md) |  | [optional] 
**connections_count** | **int** |  | [optional] 
**rules_count** | **int** |  | [optional] 
**project** | [**RouteAggregationsDataProject**](RouteAggregationsDataProject.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregations_data import RouteAggregationsData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationsData from a JSON string
route_aggregations_data_instance = RouteAggregationsData.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationsData.to_json())

# convert the object into a dict
route_aggregations_data_dict = route_aggregations_data_instance.to_dict()
# create an instance of RouteAggregationsData from a dict
route_aggregations_data_from_dict = RouteAggregationsData.from_dict(route_aggregations_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


