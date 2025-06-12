# GetAllStreamAlertRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamAlertRule]**](StreamAlertRule.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_stream_alert_rule_response import GetAllStreamAlertRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllStreamAlertRuleResponse from a JSON string
get_all_stream_alert_rule_response_instance = GetAllStreamAlertRuleResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllStreamAlertRuleResponse.to_json())

# convert the object into a dict
get_all_stream_alert_rule_response_dict = get_all_stream_alert_rule_response_instance.to_dict()
# create an instance of GetAllStreamAlertRuleResponse from a dict
get_all_stream_alert_rule_response_from_dict = GetAllStreamAlertRuleResponse.from_dict(get_all_stream_alert_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


