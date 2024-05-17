# DeviceMetro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.device_metro import DeviceMetro

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceMetro from a JSON string
device_metro_instance = DeviceMetro.from_json(json)
# print the JSON string representation of the object
print(DeviceMetro.to_json())

# convert the object into a dict
device_metro_dict = device_metro_instance.to_dict()
# create an instance of DeviceMetro from a dict
device_metro_form_dict = device_metro.from_dict(device_metro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


