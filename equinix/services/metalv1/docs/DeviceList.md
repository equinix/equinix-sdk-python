# DeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[Device]**](Device.md) |  | [optional] 
**href** | **str** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from equinix_metal.models.device_list import DeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceList from a JSON string
device_list_instance = DeviceList.from_json(json)
# print the JSON string representation of the object
print(DeviceList.to_json())

# convert the object into a dict
device_list_dict = device_list_instance.to_dict()
# create an instance of DeviceList from a dict
device_list_form_dict = device_list.from_dict(device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


