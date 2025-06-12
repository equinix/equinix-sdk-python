# MetricDatapoints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_time** | **datetime** | Datapoint end date and time | [optional] 
**start_date_time** | **datetime** | Datapoint start date and time | [optional] 
**value** | **float** | Datapoint value | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_datapoints import MetricDatapoints

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDatapoints from a JSON string
metric_datapoints_instance = MetricDatapoints.from_json(json)
# print the JSON string representation of the object
print(MetricDatapoints.to_json())

# convert the object into a dict
metric_datapoints_dict = metric_datapoints_instance.to_dict()
# create an instance of MetricDatapoints from a dict
metric_datapoints_from_dict = MetricDatapoints.from_dict(metric_datapoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


