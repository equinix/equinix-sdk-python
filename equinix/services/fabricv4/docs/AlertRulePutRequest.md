# AlertRulePutRequest

Create Stream Alert Rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer-provided stream name | [optional] 
**type** | [**AlertRulePostRequestType**](AlertRulePostRequestType.md) |  | [optional] 
**description** | **str** | Customer-provided stream description | [optional] 
**enabled** | **bool** | Stream alert rule enabled status | [optional] [default to True]
**metric_selector** | [**MetricSelector**](MetricSelector.md) |  | [optional] 
**resource_selector** | [**ResourceSelector**](ResourceSelector.md) |  | [optional] 
**detection_method** | [**DetectionMethod**](DetectionMethod.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.alert_rule_put_request import AlertRulePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRulePutRequest from a JSON string
alert_rule_put_request_instance = AlertRulePutRequest.from_json(json)
# print the JSON string representation of the object
print(AlertRulePutRequest.to_json())

# convert the object into a dict
alert_rule_put_request_dict = alert_rule_put_request_instance.to_dict()
# create an instance of AlertRulePutRequest from a dict
alert_rule_put_request_from_dict = AlertRulePutRequest.from_dict(alert_rule_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


