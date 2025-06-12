# FabricConnection

The OrchestratorProvider schema defines the configuration for a network connection and deployment properties, offering a detailed overview of the connection's characteristics and requirements. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FabricConnectionType**](FabricConnectionType.md) |  | 
**bandwidth** | **int** |  | 
**name** | **str** |  | [optional] 
**redundancy** | [**ConnectionRedundancy**](ConnectionRedundancy.md) |  | 
**a_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**z_side** | [**ConnectionSide**](ConnectionSide.md) |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_connection import FabricConnection

# TODO update the JSON string below
json = "{}"
# create an instance of FabricConnection from a JSON string
fabric_connection_instance = FabricConnection.from_json(json)
# print the JSON string representation of the object
print(FabricConnection.to_json())

# convert the object into a dict
fabric_connection_dict = fabric_connection_instance.to_dict()
# create an instance of FabricConnection from a dict
fabric_connection_from_dict = FabricConnection.from_dict(fabric_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


