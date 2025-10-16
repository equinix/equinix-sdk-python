# FabricIPWAN

The IPWAN schema defines the structure for a network IPWAN within the orchestrator system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**uuid** | **str** | Equinix-assigned access point identifier | [optional] 
**scope** | [**NetworkScope**](NetworkScope.md) |  | 
**location** | [**SimplifiedLocation**](SimplifiedLocation.md) |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_ipwan import FabricIPWAN

# TODO update the JSON string below
json = "{}"
# create an instance of FabricIPWAN from a JSON string
fabric_ipwan_instance = FabricIPWAN.from_json(json)
# print the JSON string representation of the object
print(FabricIPWAN.to_json())

# convert the object into a dict
fabric_ipwan_dict = fabric_ipwan_instance.to_dict()
# create an instance of FabricIPWAN from a dict
fabric_ipwan_from_dict = FabricIPWAN.from_dict(fabric_ipwan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


