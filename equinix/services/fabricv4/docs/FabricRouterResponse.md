# FabricRouterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Cloud Routers URI | [optional] [readonly] 
**type** | [**FabricRouterType**](FabricRouterType.md) |  | 
**uuid** | **str** | Equinix-assigned cloud router identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**name** | **str** |  | 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_router_response import FabricRouterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricRouterResponse from a JSON string
fabric_router_response_instance = FabricRouterResponse.from_json(json)
# print the JSON string representation of the object
print(FabricRouterResponse.to_json())

# convert the object into a dict
fabric_router_response_dict = fabric_router_response_instance.to_dict()
# create an instance of FabricRouterResponse from a dict
fabric_router_response_from_dict = FabricRouterResponse.from_dict(fabric_router_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


