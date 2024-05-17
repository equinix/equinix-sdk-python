# InterconnectionFabricProvider

Configuration information for connecting to external cloud service provider. Only available if the fabric_provider param was used when creating the interconnection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AWS Account ID | 
**href** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from equinix_metal.models.interconnection_fabric_provider import InterconnectionFabricProvider

# TODO update the JSON string below
json = "{}"
# create an instance of InterconnectionFabricProvider from a JSON string
interconnection_fabric_provider_instance = InterconnectionFabricProvider.from_json(json)
# print the JSON string representation of the object
print(InterconnectionFabricProvider.to_json())

# convert the object into a dict
interconnection_fabric_provider_dict = interconnection_fabric_provider_instance.to_dict()
# create an instance of InterconnectionFabricProvider from a dict
interconnection_fabric_provider_form_dict = interconnection_fabric_provider.from_dict(interconnection_fabric_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


