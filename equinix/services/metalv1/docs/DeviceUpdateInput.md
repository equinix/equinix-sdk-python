# DeviceUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_pxe** | **bool** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**customdata** | **Dict[str, object]** |  | [optional] 
**description** | **str** |  | [optional] 
**firmware_set_id** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**locked** | **bool** | Whether the device should be locked, preventing accidental deletion. | [optional] 
**network_frozen** | **bool** | If true, this instance can not be converted to a different network type. | [optional] 
**spot_instance** | **bool** | Can be set to false to convert a spot-market instance to on-demand. | [optional] 
**tags** | **List[str]** |  | [optional] 
**userdata** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.device_update_input import DeviceUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUpdateInput from a JSON string
device_update_input_instance = DeviceUpdateInput.from_json(json)
# print the JSON string representation of the object
print(DeviceUpdateInput.to_json())

# convert the object into a dict
device_update_input_dict = device_update_input_instance.to_dict()
# create an instance of DeviceUpdateInput from a dict
device_update_input_form_dict = device_update_input.from_dict(device_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


