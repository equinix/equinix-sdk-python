# FabricConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Connection URI | [optional] [readonly] 
**type** | [**FabricConnectionType**](FabricConnectionType.md) |  | 
**uuid** | **str** | Equinix-assigned connection identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**bandwidth** | **int** |  | 
**name** | **str** |  | 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_connection_response import FabricConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricConnectionResponse from a JSON string
fabric_connection_response_instance = FabricConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(FabricConnectionResponse.to_json())

# convert the object into a dict
fabric_connection_response_dict = fabric_connection_response_instance.to_dict()
# create an instance of FabricConnectionResponse from a dict
fabric_connection_response_from_dict = FabricConnectionResponse.from_dict(fabric_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


