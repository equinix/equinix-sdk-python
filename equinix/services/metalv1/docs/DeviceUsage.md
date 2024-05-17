# DeviceUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.device_usage import DeviceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsage from a JSON string
device_usage_instance = DeviceUsage.from_json(json)
# print the JSON string representation of the object
print(DeviceUsage.to_json())

# convert the object into a dict
device_usage_dict = device_usage_instance.to_dict()
# create an instance of DeviceUsage from a dict
device_usage_form_dict = device_usage.from_dict(device_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


