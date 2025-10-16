# FabricIPWANConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | IPWAN Connection URI | [optional] [readonly] 
**type** | **str** |  | [optional] 
**uuid** | **str** | Equinix-assigned ipwan connection identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | [optional] 
**bandwidth** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_ipwan_connection_response import FabricIPWANConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricIPWANConnectionResponse from a JSON string
fabric_ipwan_connection_response_instance = FabricIPWANConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(FabricIPWANConnectionResponse.to_json())

# convert the object into a dict
fabric_ipwan_connection_response_dict = fabric_ipwan_connection_response_instance.to_dict()
# create an instance of FabricIPWANConnectionResponse from a dict
fabric_ipwan_connection_response_from_dict = FabricIPWANConnectionResponse.from_dict(fabric_ipwan_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


