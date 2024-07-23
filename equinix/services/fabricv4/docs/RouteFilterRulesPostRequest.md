# RouteFilterRulesPostRequest

Create Route Filter Rule POST request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RouteFilterRulesBase]**](RouteFilterRulesBase.md) | Route Filter Rule configuration | [optional] 

## Example

```python
from equinix.services.fabricv4.models.route_filter_rules_post_request import RouteFilterRulesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteFilterRulesPostRequest from a JSON string
route_filter_rules_post_request_instance = RouteFilterRulesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RouteFilterRulesPostRequest.to_json())

# convert the object into a dict
route_filter_rules_post_request_dict = route_filter_rules_post_request_instance.to_dict()
# create an instance of RouteFilterRulesPostRequest from a dict
route_filter_rules_post_request_form_dict = route_filter_rules_post_request.from_dict(route_filter_rules_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


