# FabricIPWANResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | IPWAN URI | [optional] [readonly] 
**type** | **str** |  | [optional] 
**uuid** | **str** | Equinix-assigned IPWAN identifier | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**scope** | [**NetworkScope**](NetworkScope.md) |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.fabric_ipwan_response import FabricIPWANResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FabricIPWANResponse from a JSON string
fabric_ipwan_response_instance = FabricIPWANResponse.from_json(json)
# print the JSON string representation of the object
print(FabricIPWANResponse.to_json())

# convert the object into a dict
fabric_ipwan_response_dict = fabric_ipwan_response_instance.to_dict()
# create an instance of FabricIPWANResponse from a dict
fabric_ipwan_response_from_dict = FabricIPWANResponse.from_dict(fabric_ipwan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


