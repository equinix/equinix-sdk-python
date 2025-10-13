# FabricIPWANConnection

The OrchestratorProvider schema defines the configuration for a IPWAN connection and deployment properties, offering a detailed overview of the connection's characteristics and requirements. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**bandwidth** | **int** |  | 
**name** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.fabric_ipwan_connection import FabricIPWANConnection

# TODO update the JSON string below
json = "{}"
# create an instance of FabricIPWANConnection from a JSON string
fabric_ipwan_connection_instance = FabricIPWANConnection.from_json(json)
# print the JSON string representation of the object
print(FabricIPWANConnection.to_json())

# convert the object into a dict
fabric_ipwan_connection_dict = fabric_ipwan_connection_instance.to_dict()
# create an instance of FabricIPWANConnection from a dict
fabric_ipwan_connection_from_dict = FabricIPWANConnection.from_dict(fabric_ipwan_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


