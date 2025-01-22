# StreamAsset

Stream object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream Asset URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**type** | [**StreamAssetType**](StreamAssetType.md) |  | [optional] 
**metrics_enabled** | **bool** | enable metric | [optional] 
**attachment_status** | [**StreamAssetAttachmentStatus**](StreamAssetAttachmentStatus.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset import StreamAsset

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAsset from a JSON string
stream_asset_instance = StreamAsset.from_json(json)
# print the JSON string representation of the object
print(StreamAsset.to_json())

# convert the object into a dict
stream_asset_dict = stream_asset_instance.to_dict()
# create an instance of StreamAsset from a dict
stream_asset_from_dict = StreamAsset.from_dict(stream_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


