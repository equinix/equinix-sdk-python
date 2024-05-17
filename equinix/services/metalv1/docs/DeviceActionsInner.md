# DeviceActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.device_actions_inner import DeviceActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceActionsInner from a JSON string
device_actions_inner_instance = DeviceActionsInner.from_json(json)
# print the JSON string representation of the object
print(DeviceActionsInner.to_json())

# convert the object into a dict
device_actions_inner_dict = device_actions_inner_instance.to_dict()
# create an instance of DeviceActionsInner from a dict
device_actions_inner_form_dict = device_actions_inner.from_dict(device_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


