# GCPCloudRouterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Cloud Router id. | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | [optional] 
**type** | [**GCPCloudRouterType**](GCPCloudRouterType.md) |  | [optional] 
**vpc_id** | **str** |  | [optional] 
**subnet_id** | **str** |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gcp_cloud_router_response import GCPCloudRouterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GCPCloudRouterResponse from a JSON string
gcp_cloud_router_response_instance = GCPCloudRouterResponse.from_json(json)
# print the JSON string representation of the object
print(GCPCloudRouterResponse.to_json())

# convert the object into a dict
gcp_cloud_router_response_dict = gcp_cloud_router_response_instance.to_dict()
# create an instance of GCPCloudRouterResponse from a dict
gcp_cloud_router_response_from_dict = GCPCloudRouterResponse.from_dict(gcp_cloud_router_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


