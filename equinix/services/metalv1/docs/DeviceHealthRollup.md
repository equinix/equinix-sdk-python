# DeviceHealthRollup

Represents a Device Health Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_rollup** | **str** | Health Status | [optional] [readonly] 
**href** | **str** |  | [optional] 
**updated_at** | **datetime** | Last update of health status. | [optional] [readonly] 

## Example

```python
from equinix_metal.models.device_health_rollup import DeviceHealthRollup

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceHealthRollup from a JSON string
device_health_rollup_instance = DeviceHealthRollup.from_json(json)
# print the JSON string representation of the object
print(DeviceHealthRollup.to_json())

# convert the object into a dict
device_health_rollup_dict = device_health_rollup_instance.to_dict()
# create an instance of DeviceHealthRollup from a dict
device_health_rollup_form_dict = device_health_rollup.from_dict(device_health_rollup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


