# OrchestratorProviders

The OrchestratorProvider schema defines the structure for the orchestrator provider configuration. It includes details about the provider type and its specific configurations. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPProviderType**](GCPProviderType.md) |  | 
**resources** | [**List[GCPProviderResource]**](GCPProviderResource.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.orchestrator_providers import OrchestratorProviders

# TODO update the JSON string below
json = "{}"
# create an instance of OrchestratorProviders from a JSON string
orchestrator_providers_instance = OrchestratorProviders.from_json(json)
# print the JSON string representation of the object
print(OrchestratorProviders.to_json())

# convert the object into a dict
orchestrator_providers_dict = orchestrator_providers_instance.to_dict()
# create an instance of OrchestratorProviders from a dict
orchestrator_providers_from_dict = OrchestratorProviders.from_dict(orchestrator_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


