# GetAllStreamAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamAsset]**](StreamAsset.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_all_stream_asset_response import GetAllStreamAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllStreamAssetResponse from a JSON string
get_all_stream_asset_response_instance = GetAllStreamAssetResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllStreamAssetResponse.to_json())

# convert the object into a dict
get_all_stream_asset_response_dict = get_all_stream_asset_response_instance.to_dict()
# create an instance of GetAllStreamAssetResponse from a dict
get_all_stream_asset_response_form_dict = get_all_stream_asset_response.from_dict(get_all_stream_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


