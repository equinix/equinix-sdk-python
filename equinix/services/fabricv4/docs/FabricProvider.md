# FabricProvider

The Orchestrator Fabric Providers schema defines the structure for the orchestrator fabric provider configuration. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FabricProviderType**](FabricProviderType.md) |  | 
**resources** | [**List[FabricProviderResource]**](FabricProviderResource.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_provider import FabricProvider

# TODO update the JSON string below
json = "{}"
# create an instance of FabricProvider from a JSON string
fabric_provider_instance = FabricProvider.from_json(json)
# print the JSON string representation of the object
print(FabricProvider.to_json())

# convert the object into a dict
fabric_provider_dict = fabric_provider_instance.to_dict()
# create an instance of FabricProvider from a dict
fabric_provider_from_dict = FabricProvider.from_dict(fabric_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


