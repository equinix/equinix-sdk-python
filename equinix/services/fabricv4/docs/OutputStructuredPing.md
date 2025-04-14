# OutputStructuredPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip** | **str** |  | [optional] 
**destination_name** | **str** |  | [optional] 
**data_bytes** | **int** |  | [optional] 
**packets_transmitted** | **int** |  | [optional] 
**packets_received** | **int** |  | [optional] 
**packets_loss_percent** | **float** |  | [optional] 
**rtt_min** | **float** |  | [optional] 
**rtt_avg** | **float** |  | [optional] 
**rtt_max** | **float** |  | [optional] 
**rtt_std_dev** | **float** |  | [optional] 
**responses** | [**List[OutputStructuredPingResponseItem]**](OutputStructuredPingResponseItem.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.output_structured_ping import OutputStructuredPing

# TODO update the JSON string below
json = "{}"
# create an instance of OutputStructuredPing from a JSON string
output_structured_ping_instance = OutputStructuredPing.from_json(json)
# print the JSON string representation of the object
print(OutputStructuredPing.to_json())

# convert the object into a dict
output_structured_ping_dict = output_structured_ping_instance.to_dict()
# create an instance of OutputStructuredPing from a dict
output_structured_ping_from_dict = OutputStructuredPing.from_dict(output_structured_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


