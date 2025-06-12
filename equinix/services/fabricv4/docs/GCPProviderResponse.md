# GCPProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPProviderType**](GCPProviderType.md) |  | 
**resources** | [**List[GCPProviderResourceResponse]**](GCPProviderResourceResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gcp_provider_response import GCPProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GCPProviderResponse from a JSON string
gcp_provider_response_instance = GCPProviderResponse.from_json(json)
# print the JSON string representation of the object
print(GCPProviderResponse.to_json())

# convert the object into a dict
gcp_provider_response_dict = gcp_provider_response_instance.to_dict()
# create an instance of GCPProviderResponse from a dict
gcp_provider_response_from_dict = GCPProviderResponse.from_dict(gcp_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


