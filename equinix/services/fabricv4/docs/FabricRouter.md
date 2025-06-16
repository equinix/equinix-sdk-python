# FabricRouter

The Router schema defines the structure for a network router within the orchestrator system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FabricRouterType**](FabricRouterType.md) |  | 
**name** | **str** |  | [optional] 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**location** | [**SimplifiedLocationWithoutIBX**](SimplifiedLocationWithoutIBX.md) |  | [optional] 
**package** | [**CloudRouterPostRequestPackage**](CloudRouterPostRequestPackage.md) |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_router import FabricRouter

# TODO update the JSON string below
json = "{}"
# create an instance of FabricRouter from a JSON string
fabric_router_instance = FabricRouter.from_json(json)
# print the JSON string representation of the object
print(FabricRouter.to_json())

# convert the object into a dict
fabric_router_dict = fabric_router_instance.to_dict()
# create an instance of FabricRouter from a dict
fabric_router_from_dict = FabricRouter.from_dict(fabric_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


