# RouteAggregationRulesPostRequest

Create Route Aggregation Rule POST request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RouteAggregationRulesBase]**](RouteAggregationRulesBase.md) | Route Aggregation Rule configuration | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_aggregation_rules_post_request import RouteAggregationRulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAggregationRulesPostRequest from a JSON string
route_aggregation_rules_post_request_instance = RouteAggregationRulesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RouteAggregationRulesPostRequest.to_json())

# convert the object into a dict
route_aggregation_rules_post_request_dict = route_aggregation_rules_post_request_instance.to_dict()
# create an instance of RouteAggregationRulesPostRequest from a dict
route_aggregation_rules_post_request_from_dict = RouteAggregationRulesPostRequest.from_dict(route_aggregation_rules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


