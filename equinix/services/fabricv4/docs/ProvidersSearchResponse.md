# ProvidersSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SearchDirectConnectType**](SearchDirectConnectType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**state** | [**SearchDirectConnectState**](SearchDirectConnectState.md) |  | [optional] 
**vpc_id** | **str** |  | [optional] 
**ipv4** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.providers_search_response import ProvidersSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersSearchResponse from a JSON string
providers_search_response_instance = ProvidersSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProvidersSearchResponse.to_json())

# convert the object into a dict
providers_search_response_dict = providers_search_response_instance.to_dict()
# create an instance of ProvidersSearchResponse from a dict
providers_search_response_from_dict = ProvidersSearchResponse.from_dict(providers_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


