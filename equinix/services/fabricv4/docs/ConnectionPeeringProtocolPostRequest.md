# ConnectionPeeringProtocolPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConnectionPeeringProtocolPostRequestType**](ConnectionPeeringProtocolPostRequestType.md) |  | 
**name** | **str** | Customer-provided peering protocol name | 
**description** | **str** | Customer-provided peering protocol description | 
**customer_asn** | **int** | Customer ASN | 
**mac_address** | **str** | MAC address of the peering protocol | 
**bgp_ipv4** | [**PeeringConnectionIpv4**](PeeringConnectionIpv4.md) |  | 
**bgp_ipv6** | [**PeeringConnectionIpv6**](PeeringConnectionIpv6.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.connection_peering_protocol_post_request import ConnectionPeeringProtocolPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPeeringProtocolPostRequest from a JSON string
connection_peering_protocol_post_request_instance = ConnectionPeeringProtocolPostRequest.from_json(json)
# print the JSON string representation of the object
print(ConnectionPeeringProtocolPostRequest.to_json())

# convert the object into a dict
connection_peering_protocol_post_request_dict = connection_peering_protocol_post_request_instance.to_dict()
# create an instance of ConnectionPeeringProtocolPostRequest from a dict
connection_peering_protocol_post_request_from_dict = ConnectionPeeringProtocolPostRequest.from_dict(connection_peering_protocol_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


