# BandwidthUtilization

Bandwidth utilization statistics (octet counters-based)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | [**BandwidthUtilizationUnit**](BandwidthUtilizationUnit.md) |  | [optional] 
**metric_interval** | **str** | An interval formatted value, indicating the time-interval the metric objects within the response represent | [optional] 
**inbound** | [**Direction**](Direction.md) |  | [optional] 
**outbound** | [**Direction**](Direction.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bandwidth_utilization import BandwidthUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthUtilization from a JSON string
bandwidth_utilization_instance = BandwidthUtilization.from_json(json)
# print the JSON string representation of the object
print(BandwidthUtilization.to_json())

# convert the object into a dict
bandwidth_utilization_dict = bandwidth_utilization_instance.to_dict()
# create an instance of BandwidthUtilization from a dict
bandwidth_utilization_form_dict = bandwidth_utilization.from_dict(bandwidth_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


