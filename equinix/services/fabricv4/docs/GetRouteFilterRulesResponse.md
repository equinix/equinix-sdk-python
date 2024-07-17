# GetRouteFilterRulesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFilterRulesData]**](RouteFilterRulesData.md) | List of Route Filter Rules | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_route_filter_rules_response import GetRouteFilterRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteFilterRulesResponse from a JSON string
get_route_filter_rules_response_instance = GetRouteFilterRulesResponse.from_json(json)
# print the JSON string representation of the object
print(GetRouteFilterRulesResponse.to_json())

# convert the object into a dict
get_route_filter_rules_response_dict = get_route_filter_rules_response_instance.to_dict()
# create an instance of GetRouteFilterRulesResponse from a dict
get_route_filter_rules_response_form_dict = get_route_filter_rules_response.from_dict(get_route_filter_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


