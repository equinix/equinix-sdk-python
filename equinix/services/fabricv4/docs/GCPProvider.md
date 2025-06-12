# GCPProvider

The Orchestrator GCP Providers schema defines the structure for the orchestrator gcp provider configuration. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPProviderType**](GCPProviderType.md) |  | 
**resources** | [**List[GCPProviderResource]**](GCPProviderResource.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.gcp_provider import GCPProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GCPProvider from a JSON string
gcp_provider_instance = GCPProvider.from_json(json)
# print the JSON string representation of the object
print(GCPProvider.to_json())

# convert the object into a dict
gcp_provider_dict = gcp_provider_instance.to_dict()
# create an instance of GCPProvider from a dict
gcp_provider_from_dict = GCPProvider.from_dict(gcp_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


