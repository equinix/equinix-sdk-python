# FabricProviderResponse

The response from the orchestrator when querying for fabric provider resources. This response contains a list of resources that are managed by the fabric provider. The resources can be routers, connections, or route protocols. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FabricProviderType**](FabricProviderType.md) |  | 
**resources** | [**List[FabricProviderResourceResponse]**](FabricProviderResourceResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_provider_response import FabricProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricProviderResponse from a JSON string
fabric_provider_response_instance = FabricProviderResponse.from_json(json)
# print the JSON string representation of the object
print(FabricProviderResponse.to_json())

# convert the object into a dict
fabric_provider_response_dict = fabric_provider_response_instance.to_dict()
# create an instance of FabricProviderResponse from a dict
fabric_provider_response_from_dict = FabricProviderResponse.from_dict(fabric_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


