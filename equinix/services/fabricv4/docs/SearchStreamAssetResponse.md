# SearchStreamAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[StreamSearchAsset]**](StreamSearchAsset.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_stream_asset_response import SearchStreamAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStreamAssetResponse from a JSON string
search_stream_asset_response_instance = SearchStreamAssetResponse.from_json(json)
# print the JSON string representation of the object
print(SearchStreamAssetResponse.to_json())

# convert the object into a dict
search_stream_asset_response_dict = search_stream_asset_response_instance.to_dict()
# create an instance of SearchStreamAssetResponse from a dict
search_stream_asset_response_from_dict = SearchStreamAssetResponse.from_dict(search_stream_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


