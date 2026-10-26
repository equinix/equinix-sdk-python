# StreamAssetInterface

Network Edge Device interface attached to a stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Network Edge Device interface URI | [optional] [readonly] 
**id** | **int** | Network Edge Device interface identifier | [optional] 
**uuid** | **str** | Network Edge Device interface UUID | [optional] 
**type** | [**StreamAssetInterfaceType**](StreamAssetInterfaceType.md) |  | [optional] 
**state** | **str** | Network Edge Device interface usage status | [optional] 
**attachment_status** | [**StreamAssetInterfaceAttachmentStatus**](StreamAssetInterfaceAttachmentStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_interface import StreamAssetInterface

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetInterface from a JSON string
stream_asset_interface_instance = StreamAssetInterface.from_json(json)
# print the JSON string representation of the object
print(StreamAssetInterface.to_json())

# convert the object into a dict
stream_asset_interface_dict = stream_asset_interface_instance.to_dict()
# create an instance of StreamAssetInterface from a dict
stream_asset_interface_from_dict = StreamAssetInterface.from_dict(stream_asset_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


