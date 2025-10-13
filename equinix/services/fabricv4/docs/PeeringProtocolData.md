# PeeringProtocolData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Peering Protocol URI | [optional] 
**uuid** | **str** | Peering protocol identifier | [optional] 
**type** | [**PeeringProtocolDataType**](PeeringProtocolDataType.md) |  | [optional] 
**name** | **str** | Protocol Name | [optional] 
**description** | **str** | Protocol Description | [optional] 
**customer_asn** | **int** | Customer ASN | [optional] 
**equinix_asn** | **int** | Equinix ASN | [optional] 
**state** | [**PeeringProtocolDataState**](PeeringProtocolDataState.md) |  | [optional] 
**mac_address** | **str** | MAC Address of The Peering Protocol | [optional] 
**bgp_ipv4** | [**PeeringConnectionResIpv4**](PeeringConnectionResIpv4.md) |  | [optional] 
**bgp_ipv6** | [**PeeringConnectionResIpv6**](PeeringConnectionResIpv6.md) |  | [optional] 
**route_collectors** | [**PeeringProtocolDataRouteCollectors**](PeeringProtocolDataRouteCollectors.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_protocol_data import PeeringProtocolData

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringProtocolData from a JSON string
peering_protocol_data_instance = PeeringProtocolData.from_json(json)
# print the JSON string representation of the object
print(PeeringProtocolData.to_json())

# convert the object into a dict
peering_protocol_data_dict = peering_protocol_data_instance.to_dict()
# create an instance of PeeringProtocolData from a dict
peering_protocol_data_from_dict = PeeringProtocolData.from_dict(peering_protocol_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


