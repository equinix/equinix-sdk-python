# RouteAggregationRulesSearchRequest

Search route aggregation rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**RouteAggregationRulesFilter**](RouteAggregationRulesFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[RouteAggregationRuleSortCriteria]**](RouteAggregationRuleSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_search_request import RouteAggregationRulesSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesSearchRequest from a JSON string
route_aggregation_rules_search_request_instance = RouteAggregationRulesSearchRequest.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesSearchRequest.to_json())

# convert the object into a dict
route_aggregation_rules_search_request_dict = route_aggregation_rules_search_request_instance.to_dict()
# create an instance of RouteAggregationRulesSearchRequest from a dict
route_aggregation_rules_search_request_from_dict = RouteAggregationRulesSearchRequest.from_dict(route_aggregation_rules_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


