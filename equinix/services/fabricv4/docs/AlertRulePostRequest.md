# AlertRulePostRequest

Create Stream Alert Rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AlertRulePostRequestType**](AlertRulePostRequestType.md) |  | 
**name** | **str** | Customer-provided stream name | 
**description** | **str** | Customer-provided stream description | [optional] 
**enabled** | **bool** | Stream alert rule enabled status | [optional] [default to True]
**metric_selector** | [**MetricSelector**](MetricSelector.md) |  | 
**resource_selector** | [**ResourceSelector**](ResourceSelector.md) |  | 
**detection_method** | [**DetectionMethod**](DetectionMethod.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.alert_rule_post_request import AlertRulePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRulePostRequest from a JSON string
alert_rule_post_request_instance = AlertRulePostRequest.from_json(json)
# print the JSON string representation of the object
print(AlertRulePostRequest.to_json())

# convert the object into a dict
alert_rule_post_request_dict = alert_rule_post_request_instance.to_dict()
# create an instance of AlertRulePostRequest from a dict
alert_rule_post_request_from_dict = AlertRulePostRequest.from_dict(alert_rule_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


