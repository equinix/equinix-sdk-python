# GetMetricsByAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[Metric]**](Metric.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_metrics_by_asset_response import GetMetricsByAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsByAssetResponse from a JSON string
get_metrics_by_asset_response_instance = GetMetricsByAssetResponse.from_json(json)
# print the JSON string representation of the object
print(GetMetricsByAssetResponse.to_json())

# convert the object into a dict
get_metrics_by_asset_response_dict = get_metrics_by_asset_response_instance.to_dict()
# create an instance of GetMetricsByAssetResponse from a dict
get_metrics_by_asset_response_from_dict = GetMetricsByAssetResponse.from_dict(get_metrics_by_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


