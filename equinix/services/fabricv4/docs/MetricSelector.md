# MetricSelector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Stream alert rule filtered by metric name | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_selector import MetricSelector

# TODO update the JSON string below
json = "{}"
# create an instance of MetricSelector from a JSON string
metric_selector_instance = MetricSelector.from_json(json)
# print the JSON string representation of the object
print(MetricSelector.to_json())

# convert the object into a dict
metric_selector_dict = metric_selector_instance.to_dict()
# create an instance of MetricSelector from a dict
metric_selector_from_dict = MetricSelector.from_dict(metric_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


