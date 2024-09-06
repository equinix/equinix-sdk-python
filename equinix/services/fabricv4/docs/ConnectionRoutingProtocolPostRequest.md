# ConnectionRoutingProtocolPostRequest

Create connection routing protocolpost request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoutingProtocolBase]**](RoutingProtocolBase.md) | Connection routing protocol configuration | [optional] 

## Example

```python
from equinix.services.fabricv4.models.connection_routing_protocol_post_request import ConnectionRoutingProtocolPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionRoutingProtocolPostRequest from a JSON string
connection_routing_protocol_post_request_instance = ConnectionRoutingProtocolPostRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionRoutingProtocolPostRequest.to_json())

# convert the object into a dict
connection_routing_protocol_post_request_dict = connection_routing_protocol_post_request_instance.to_dict()
# create an instance of ConnectionRoutingProtocolPostRequest from a dict
connection_routing_protocol_post_request_from_dict = ConnectionRoutingProtocolPostRequest.from_dict(connection_routing_protocol_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


