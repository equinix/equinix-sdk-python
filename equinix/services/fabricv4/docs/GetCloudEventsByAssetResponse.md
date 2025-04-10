# GetCloudEventsByAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**data** | [**List[CloudEvent]**](CloudEvent.md) | Data returned from the API call. | [optional] 

## Example

```python
from equinix.services.fabricv4.models.get_cloud_events_by_asset_response import GetCloudEventsByAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCloudEventsByAssetResponse from a JSON string
get_cloud_events_by_asset_response_instance = GetCloudEventsByAssetResponse.from_json(json)
# print the JSON string representation of the object
print(GetCloudEventsByAssetResponse.to_json())

# convert the object into a dict
get_cloud_events_by_asset_response_dict = get_cloud_events_by_asset_response_instance.to_dict()
# create an instance of GetCloudEventsByAssetResponse from a dict
get_cloud_events_by_asset_response_from_dict = GetCloudEventsByAssetResponse.from_dict(get_cloud_events_by_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


