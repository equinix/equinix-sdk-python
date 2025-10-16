# MetricFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[MetricSimpleExpression]**](MetricSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.metric_filters import MetricFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MetricFilters from a JSON string
metric_filters_instance = MetricFilters.from_json(json)
# print the JSON string representation of the object
print(MetricFilters.to_json())

# convert the object into a dict
metric_filters_dict = metric_filters_instance.to_dict()
# create an instance of MetricFilters from a dict
metric_filters_from_dict = MetricFilters.from_dict(metric_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


