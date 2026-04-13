# RouteFilterRulesSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFilterRulesData]**](RouteFilterRulesData.md) | List of route filter rules | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_search_response import RouteFilterRulesSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesSearchResponse from a JSON string
route_filter_rules_search_response_instance = RouteFilterRulesSearchResponse.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesSearchResponse.to_json())

# convert the object into a dict
route_filter_rules_search_response_dict = route_filter_rules_search_response_instance.to_dict()
# create an instance of RouteFilterRulesSearchResponse from a dict
route_filter_rules_search_response_from_dict = RouteFilterRulesSearchResponse.from_dict(route_filter_rules_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


