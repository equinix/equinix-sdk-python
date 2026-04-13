# RouteAggregationRulesSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationRulesData]**](RouteAggregationRulesData.md) | List of route aggregation rules | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_search_response import RouteAggregationRulesSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesSearchResponse from a JSON string
route_aggregation_rules_search_response_instance = RouteAggregationRulesSearchResponse.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesSearchResponse.to_json())

# convert the object into a dict
route_aggregation_rules_search_response_dict = route_aggregation_rules_search_response_instance.to_dict()
# create an instance of RouteAggregationRulesSearchResponse from a dict
route_aggregation_rules_search_response_from_dict = RouteAggregationRulesSearchResponse.from_dict(route_aggregation_rules_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


