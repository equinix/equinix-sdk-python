# StreamAssetPutRequest

Update Stream Asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics_enabled** | **bool** | enable metric | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_put_request import StreamAssetPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetPutRequest from a JSON string
stream_asset_put_request_instance = StreamAssetPutRequest.from_json(json)
# print the JSON string representation of the object
print(StreamAssetPutRequest.to_json())

# convert the object into a dict
stream_asset_put_request_dict = stream_asset_put_request_instance.to_dict()
# create an instance of StreamAssetPutRequest from a dict
stream_asset_put_request_form_dict = stream_asset_put_request.from_dict(stream_asset_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


