# StreamDevicePutRequest

Attach Network Edge Device interfaces to a Stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics_enabled** | **bool** | enable metric. Must be true when interfaces are provided | [optional] [default to False]
**interfaces** | [**List[StreamDeviceInterfaceRequest]**](StreamDeviceInterfaceRequest.md) | Complete desired set of Network Edge Device interfaces attached to the stream. Interfaces not in the list are detached; an empty or absent list detaches all interfaces.  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_device_put_request import StreamDevicePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamDevicePutRequest from a JSON string
stream_device_put_request_instance = StreamDevicePutRequest.from_json(json)
# print the JSON string representation of the object
print(StreamDevicePutRequest.to_json())

# convert the object into a dict
stream_device_put_request_dict = stream_device_put_request_instance.to_dict()
# create an instance of StreamDevicePutRequest from a dict
stream_device_put_request_from_dict = StreamDevicePutRequest.from_dict(stream_device_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


