# RouteFilterRulesChangeDataResponse

List of Route Filter Rule changes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[RouteFilterRulesChangeData]**](RouteFilterRulesChangeData.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_change_data_response import RouteFilterRulesChangeDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesChangeDataResponse from a JSON string
route_filter_rules_change_data_response_instance = RouteFilterRulesChangeDataResponse.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesChangeDataResponse.to_json())

# convert the object into a dict
route_filter_rules_change_data_response_dict = route_filter_rules_change_data_response_instance.to_dict()
# create an instance of RouteFilterRulesChangeDataResponse from a dict
route_filter_rules_change_data_response_from_dict = RouteFilterRulesChangeDataResponse.from_dict(route_filter_rules_change_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


