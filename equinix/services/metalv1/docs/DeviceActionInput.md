# DeviceActionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprovision_fast** | **bool** | When type is &#x60;reinstall&#x60;, enabling fast deprovisioning will bypass full disk wiping. | [optional] 
**force_delete** | **bool** | May be required to perform actions under certain conditions | [optional] 
**href** | **str** |  | [optional] 
**ipxe_script_url** | **str** | When type is &#x60;reinstall&#x60;, use this &#x60;ipxe_script_url&#x60; (&#x60;operating_system&#x60; must be &#x60;custom_ipxe&#x60;, defaults to the current &#x60;ipxe_script_url&#x60;) | [optional] 
**operating_system** | **str** | When type is &#x60;reinstall&#x60;, use this &#x60;operating_system&#x60; (defaults to the current &#x60;operating system&#x60;) | [optional] 
**preserve_data** | **bool** | When type is &#x60;reinstall&#x60;, preserve the existing data on all disks except the operating-system disk. | [optional] 
**type** | **str** | Action to perform. See Device.actions for possible actions. | 

## Example

```python
from equinix_metal.models.device_action_input import DeviceActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceActionInput from a JSON string
device_action_input_instance = DeviceActionInput.from_json(json)
# print the JSON string representation of the object
print(DeviceActionInput.to_json())

# convert the object into a dict
device_action_input_dict = device_action_input_instance.to_dict()
# create an instance of DeviceActionInput from a dict
device_action_input_form_dict = device_action_input.from_dict(device_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


