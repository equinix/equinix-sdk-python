# StreamAssetSortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**StreamAssetSortDirection**](StreamAssetSortDirection.md) |  | [optional] 
**var_property** | [**StreamAssetSortBy**](StreamAssetSortBy.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.stream_asset_sort_criteria import StreamAssetSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of StreamAssetSortCriteria from a JSON string
stream_asset_sort_criteria_instance = StreamAssetSortCriteria.from_json(json)
# print the JSON string representation of the object
print(StreamAssetSortCriteria.to_json())

# convert the object into a dict
stream_asset_sort_criteria_dict = stream_asset_sort_criteria_instance.to_dict()
# create an instance of StreamAssetSortCriteria from a dict
stream_asset_sort_criteria_form_dict = stream_asset_sort_criteria.from_dict(stream_asset_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


