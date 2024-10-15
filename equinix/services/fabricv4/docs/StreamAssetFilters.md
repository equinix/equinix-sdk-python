# StreamAssetFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[StreamAssetFilter]**](StreamAssetFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_filters import StreamAssetFilters

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetFilters from a JSON string
stream_asset_filters_instance = StreamAssetFilters.from_json(json)
# print the JSON string representation of the object
print(StreamAssetFilters.to_json())

# convert the object into a dict
stream_asset_filters_dict = stream_asset_filters_instance.to_dict()
# create an instance of StreamAssetFilters from a dict
stream_asset_filters_form_dict = stream_asset_filters.from_dict(stream_asset_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


