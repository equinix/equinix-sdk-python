# StreamAlertRule

Stream object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream Alert Rule URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**type** | [**StreamAlertRuleType**](StreamAlertRuleType.md) |  | [optional] 
**name** | **str** | Customer-provided stream alert rule name | [optional] 
**description** | **str** | Customer-provided stream alert rule description | [optional] 
**state** | [**StreamAlertRuleState**](StreamAlertRuleState.md) |  | [optional] 
**enabled** | **bool** | Stream alert rule enabled status | [optional] [default to True]
**metric_name** | **str** | Stream alert rule metric name | [optional] 
**resource_selector** | [**ResourceSelector**](ResourceSelector.md) |  | [optional] 
**window_size** | **str** | Stream alert rule metric window size | [optional] 
**operand** | [**AlertRulePostRequestOperand**](AlertRulePostRequestOperand.md) |  | [optional] 
**warning_threshold** | **str** | Stream alert rule metric warning threshold | [optional] 
**critical_threshold** | **str** | Stream alert rule metric critical threshold | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_alert_rule import StreamAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAlertRule from a JSON string
stream_alert_rule_instance = StreamAlertRule.from_json(json)
# print the JSON string representation of the object
print(StreamAlertRule.to_json())

# convert the object into a dict
stream_alert_rule_dict = stream_alert_rule_instance.to_dict()
# create an instance of StreamAlertRule from a dict
stream_alert_rule_from_dict = StreamAlertRule.from_dict(stream_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


