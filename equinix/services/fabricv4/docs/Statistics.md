# Statistics

This API provides service-level traffic metrics so that you can view access and gather key information required to manage service subscription sizing and capacity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** | Start and duration of the statistical analysis interval. | [optional] 
**end_date_time** | **datetime** | End and duration of the statistical analysis interval. | [optional] 
**view_point** | [**StatisticsViewPoint**](StatisticsViewPoint.md) |  | [optional] 
**bandwidth_utilization** | [**BandwidthUtilization**](BandwidthUtilization.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.statistics import Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of Statistics from a JSON string
statistics_instance = Statistics.from_json(json)
# print the JSON string representation of the object
print(Statistics.to_json())

# convert the object into a dict
statistics_dict = statistics_instance.to_dict()
# create an instance of Statistics from a dict
statistics_from_dict = Statistics.from_dict(statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


