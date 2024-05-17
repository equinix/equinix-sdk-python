# DeviceUsageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**usages** | [**List[DeviceUsage]**](DeviceUsage.md) |  | [optional] 

## Example

```python
from equinix_metal.models.device_usage_list import DeviceUsageList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsageList from a JSON string
device_usage_list_instance = DeviceUsageList.from_json(json)
# print the JSON string representation of the object
print(DeviceUsageList.to_json())

# convert the object into a dict
device_usage_list_dict = device_usage_list_instance.to_dict()
# create an instance of DeviceUsageList from a dict
device_usage_list_form_dict = device_usage_list.from_dict(device_usage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


