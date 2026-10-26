# StreamDeviceInterfaceRequest

Network Edge Device interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Network Edge Device interface identifier | 

## Example

```python
from equinix.services.fabricv4.models.stream_device_interface_request import StreamDeviceInterfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamDeviceInterfaceRequest from a JSON string
stream_device_interface_request_instance = StreamDeviceInterfaceRequest.from_json(json)
# print the JSON string representation of the object
print(StreamDeviceInterfaceRequest.to_json())

# convert the object into a dict
stream_device_interface_request_dict = stream_device_interface_request_instance.to_dict()
# create an instance of StreamDeviceInterfaceRequest from a dict
stream_device_interface_request_from_dict = StreamDeviceInterfaceRequest.from_dict(stream_device_interface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


