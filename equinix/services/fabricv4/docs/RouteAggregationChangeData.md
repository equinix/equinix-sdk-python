# RouteAggregationChangeData

Current state of latest Route Aggregation change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current outcome of the change flow | [optional] 
**created_by** | **str** | Created by User Key | [optional] 
**created_date_time** | **datetime** | Set when change flow starts | [optional] 
**updated_by** | **str** | Updated by User Key | [optional] 
**updated_date_time** | **datetime** | Set when change object is updated | [optional] 
**information** | **str** | Additional information | [optional] 
**data** | [**RouteAggregationsChangeOperation**](RouteAggregationsChangeOperation.md) |  | [optional] 
**uuid** | **str** | Uniquely identifies a change | 
**type** | [**RouteAggregationsChangeType**](RouteAggregationsChangeType.md) |  | 
**href** | **str** | Route AGGREGATION Change URI | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_change_data import RouteAggregationChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationChangeData from a JSON string
route_aggregation_change_data_instance = RouteAggregationChangeData.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationChangeData.to_json())

# convert the object into a dict
route_aggregation_change_data_dict = route_aggregation_change_data_instance.to_dict()
# create an instance of RouteAggregationChangeData from a dict
route_aggregation_change_data_form_dict = route_aggregation_change_data.from_dict(route_aggregation_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


