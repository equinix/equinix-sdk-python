# StreamAssetSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**StreamAssetFilters**](StreamAssetFilters.md) |  | 
**pagination** | [**PaginationRequest**](PaginationRequest.md) |  | [optional] 
**sort** | [**List[StreamAssetSortCriteria]**](StreamAssetSortCriteria.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_search_request import StreamAssetSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetSearchRequest from a JSON string
stream_asset_search_request_instance = StreamAssetSearchRequest.from_json(json)
# print the JSON string representation of the object
print(StreamAssetSearchRequest.to_json())

# convert the object into a dict
stream_asset_search_request_dict = stream_asset_search_request_instance.to_dict()
# create an instance of StreamAssetSearchRequest from a dict
stream_asset_search_request_from_dict = StreamAssetSearchRequest.from_dict(stream_asset_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


