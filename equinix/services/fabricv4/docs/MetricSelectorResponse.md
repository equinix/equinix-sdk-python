# MetricSelectorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Stream alert rule filtered by metric name | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_selector_response import MetricSelectorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MetricSelectorResponse from a JSON string
metric_selector_response_instance = MetricSelectorResponse.from_json(json)
# print the JSON string representation of the object
print(MetricSelectorResponse.to_json())

# convert the object into a dict
metric_selector_response_dict = metric_selector_response_instance.to_dict()
# create an instance of MetricSelectorResponse from a dict
metric_selector_response_from_dict = MetricSelectorResponse.from_dict(metric_selector_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


