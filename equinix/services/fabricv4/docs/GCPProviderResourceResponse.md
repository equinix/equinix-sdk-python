# GCPProviderResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GCPCloudRouterType**](GCPCloudRouterType.md) |  | 
**project_id** | **str** |  | 
**provider_id** | **str** |  | 
**pool_id** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**id** | **str** | Cloud Router id. | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | [optional] 
**vpc_id** | **str** |  | [optional] 
**subnet_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gcp_provider_resource_response import GCPProviderResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GCPProviderResourceResponse from a JSON string
gcp_provider_resource_response_instance = GCPProviderResourceResponse.from_json(json)
# print the JSON string representation of the object
print(GCPProviderResourceResponse.to_json())

# convert the object into a dict
gcp_provider_resource_response_dict = gcp_provider_resource_response_instance.to_dict()
# create an instance of GCPProviderResourceResponse from a dict
gcp_provider_resource_response_from_dict = GCPProviderResourceResponse.from_dict(gcp_provider_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


