# GCPProviderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPCloudRouterType**](GCPCloudRouterType.md) |  | 
**project_id** | **str** |  | 
**provider_id** | **str** |  | 
**pool_id** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**vpc_id** | **str** |  | 
**subnet_id** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.gcp_provider_resource import GCPProviderResource

# TODO update the JSON string below
json = "{}"
# create an instance of GCPProviderResource from a JSON string
gcp_provider_resource_instance = GCPProviderResource.from_json(json)
# print the JSON string representation of the object
print(GCPProviderResource.to_json())

# convert the object into a dict
gcp_provider_resource_dict = gcp_provider_resource_instance.to_dict()
# create an instance of GCPProviderResource from a dict
gcp_provider_resource_from_dict = GCPProviderResource.from_dict(gcp_provider_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


