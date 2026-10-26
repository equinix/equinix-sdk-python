# RoutingProtocolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_asn** | **int** | Customer Autonomous System Number (ASN) | [optional] 
**mac_address** | **str** | MAC address of the customer interface | [optional] 
**bgp_ipv4** | [**ExchangeServiceRequestBgp**](ExchangeServiceRequestBgp.md) |  | [optional] 
**bgp_ipv6** | [**ExchangeServiceRequestBgp**](ExchangeServiceRequestBgp.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.routing_protocol_request import RoutingProtocolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingProtocolRequest from a JSON string
routing_protocol_request_instance = RoutingProtocolRequest.from_json(json)
# print the JSON string representation of the object
print(RoutingProtocolRequest.to_json())

# convert the object into a dict
routing_protocol_request_dict = routing_protocol_request_instance.to_dict()
# create an instance of RoutingProtocolRequest from a dict
routing_protocol_request_from_dict = RoutingProtocolRequest.from_dict(routing_protocol_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


