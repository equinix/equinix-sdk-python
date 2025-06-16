# MetricResource

Metric resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Metric resource href | [optional] 
**uuid** | **str** | Metric resource UUID | [optional] 
**type** | **str** | Metric resource type | [optional] 
**name** | **str** | Metric resource name | [optional] 
**description** | **str** | Metric resource description | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_resource import MetricResource

# TODO update the JSON string below
json = "{}"
# create an instance of MetricResource from a JSON string
metric_resource_instance = MetricResource.from_json(json)
# print the JSON string representation of the object
print(MetricResource.to_json())

# convert the object into a dict
metric_resource_dict = metric_resource_instance.to_dict()
# create an instance of MetricResource from a dict
metric_resource_from_dict = MetricResource.from_dict(metric_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


