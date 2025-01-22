# Metrics

Bandwidth utilization statistics for a specified interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_end_timestamp** | **datetime** | Interval end timestamp | [optional] 
**max** | **float** | Max bandwidth within statistics object time interval, represented in units specified by response \&quot;units\&quot; field | [optional] 
**mean** | **float** | Mean bandwidth within statistics object time interval, represented in units specified by response \&quot;units\&quot; field | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metrics import Metrics

# TODO update the JSON string below
json = "{}"
# create an instance of Metrics from a JSON string
metrics_instance = Metrics.from_json(json)
# print the JSON string representation of the object
print(Metrics.to_json())

# convert the object into a dict
metrics_dict = metrics_instance.to_dict()
# create an instance of Metrics from a dict
metrics_from_dict = Metrics.from_dict(metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


