# RouteAggregationRulesChangeDataResponse

List of Route Aggregation Rule changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationRulesChangeData]**](RouteAggregationRulesChangeData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_change_data_response import RouteAggregationRulesChangeDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesChangeDataResponse from a JSON string
route_aggregation_rules_change_data_response_instance = RouteAggregationRulesChangeDataResponse.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesChangeDataResponse.to_json())

# convert the object into a dict
route_aggregation_rules_change_data_response_dict = route_aggregation_rules_change_data_response_instance.to_dict()
# create an instance of RouteAggregationRulesChangeDataResponse from a dict
route_aggregation_rules_change_data_response_from_dict = RouteAggregationRulesChangeDataResponse.from_dict(route_aggregation_rules_change_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


