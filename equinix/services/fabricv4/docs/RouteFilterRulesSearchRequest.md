# RouteFilterRulesSearchRequest

Search route filter rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**RouteFilterRulesFilter**](RouteFilterRulesFilter.md) |  | [optional] 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[RouteFilterRuleSortCriteria]**](RouteFilterRuleSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_search_request import RouteFilterRulesSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesSearchRequest from a JSON string
route_filter_rules_search_request_instance = RouteFilterRulesSearchRequest.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesSearchRequest.to_json())

# convert the object into a dict
route_filter_rules_search_request_dict = route_filter_rules_search_request_instance.to_dict()
# create an instance of RouteFilterRulesSearchRequest from a dict
route_filter_rules_search_request_from_dict = RouteFilterRulesSearchRequest.from_dict(route_filter_rules_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


