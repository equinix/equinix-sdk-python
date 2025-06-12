# Metric

Metric object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Equinix supported metric type | [optional] 
**name** | **str** | Metric name | [optional] 
**unit** | **str** | Metric unit | [optional] 
**resource** | [**MetricResource**](MetricResource.md) |  | [optional] 
**summary** | **str** | Metric summary | [optional] 
**datapoints** | [**List[MetricDatapoints]**](MetricDatapoints.md) | Metric data points | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric import Metric

# TODO update the JSON string below
json = "{}"
# create an instance of Metric from a JSON string
metric_instance = Metric.from_json(json)
# print the JSON string representation of the object
print(Metric.to_json())

# convert the object into a dict
metric_dict = metric_instance.to_dict()
# create an instance of Metric from a dict
metric_from_dict = Metric.from_dict(metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


