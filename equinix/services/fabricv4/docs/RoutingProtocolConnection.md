# RoutingProtocolConnection

Connection specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Equinix-assigned connection identifier | [optional] 
**platform_uuid** | **str** | Equinix-assigned platform connection identifier | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_connection import RoutingProtocolConnection

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolConnection from a JSON string
routing_protocol_connection_instance = RoutingProtocolConnection.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolConnection.to_json())

# convert the object into a dict
routing_protocol_connection_dict = routing_protocol_connection_instance.to_dict()
# create an instance of RoutingProtocolConnection from a dict
routing_protocol_connection_from_dict = RoutingProtocolConnection.from_dict(routing_protocol_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


