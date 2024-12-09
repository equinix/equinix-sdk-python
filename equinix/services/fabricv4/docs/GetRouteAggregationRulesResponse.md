# GetRouteAggregationRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteAggregationRulesData]**](RouteAggregationRulesData.md) | List of Route Aggregation Rules | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_route_aggregation_rules_response import GetRouteAggregationRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteAggregationRulesResponse from a JSON string
get_route_aggregation_rules_response_instance = GetRouteAggregationRulesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRouteAggregationRulesResponse.to_json())

# convert the object into a dict
get_route_aggregation_rules_response_dict = get_route_aggregation_rules_response_instance.to_dict()
# create an instance of GetRouteAggregationRulesResponse from a dict
get_route_aggregation_rules_response_form_dict = get_route_aggregation_rules_response.from_dict(get_route_aggregation_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


