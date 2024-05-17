# FindTrafficTimeframeParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ended_at** | **datetime** |  | 
**href** | **str** |  | [optional] 
**started_at** | **datetime** |  | 

## Example

```python
from equinix_metal.models.find_traffic_timeframe_parameter import FindTrafficTimeframeParameter

# TODO update the JSON string below
json = "{}"
# create an instance of FindTrafficTimeframeParameter from a JSON string
find_traffic_timeframe_parameter_instance = FindTrafficTimeframeParameter.from_json(json)
# print the JSON string representation of the object
print(FindTrafficTimeframeParameter.to_json())

# convert the object into a dict
find_traffic_timeframe_parameter_dict = find_traffic_timeframe_parameter_instance.to_dict()
# create an instance of FindTrafficTimeframeParameter from a dict
find_traffic_timeframe_parameter_form_dict = find_traffic_timeframe_parameter.from_dict(find_traffic_timeframe_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


