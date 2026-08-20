# StreamSearchAsset

Stream object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Stream Asset URI | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**stream_uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**type** | **str** | Asset type | [optional] 
**metrics_enabled** | **bool** | enable metric | [optional] 
**attachment_status** | [**StreamAssetAttachmentStatus**](StreamAssetAttachmentStatus.md) |  | [optional] 
**project_id** | **str** | project ic | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_search_asset import StreamSearchAsset

# TODO update the JSON string below
json = "{}"
# create an instance of StreamSearchAsset from a JSON string
stream_search_asset_instance = StreamSearchAsset.from_json(json)
# print the JSON string representation of the object
print(StreamSearchAsset.to_json())

# convert the object into a dict
stream_search_asset_dict = stream_search_asset_instance.to_dict()
# create an instance of StreamSearchAsset from a dict
stream_search_asset_from_dict = StreamSearchAsset.from_dict(stream_search_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


