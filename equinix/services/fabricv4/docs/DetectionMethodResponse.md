# DetectionMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DetectionMethodType**](DetectionMethodType.md) |  | [optional] 
**window_size** | **str** | Stream alert rule metric window size | [optional] 
**operand** | [**DetectionMethodOperand**](DetectionMethodOperand.md) |  | [optional] 
**warning_threshold** | **str** | Stream alert rule metric warning threshold | [optional] 
**critical_threshold** | **str** | Stream alert rule metric critical threshold | [optional] 

## Example

```python
from equinix.services.fabricv4.models.detection_method_response import DetectionMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionMethodResponse from a JSON string
detection_method_response_instance = DetectionMethodResponse.from_json(json)
# print the JSON string representation of the object
print(DetectionMethodResponse.to_json())

# convert the object into a dict
detection_method_response_dict = detection_method_response_instance.to_dict()
# create an instance of DetectionMethodResponse from a dict
detection_method_response_from_dict = DetectionMethodResponse.from_dict(detection_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


