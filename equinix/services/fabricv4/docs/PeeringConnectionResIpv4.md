# PeeringConnectionResIpv4

BGP IPv4 Connection Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** | Customer peer IPv4 address | [optional] 
**primary_equinix_peer_ip** | **str** | Primary Equinix peer IPv4 address | [optional] 
**secondary_equinix_peer_ip** | **str** | Secondary Equinix peer IPv4 address | [optional] 
**reverse_dns_address** | **str** | Reverse DNS address for the BGP session | [optional] 
**as_set** | **str** | Autonomous System Set for the BGP session | [optional] 
**mlpe_enabled** | **bool** | Whether MLPE is enabled for the BGP session | [optional] 
**auth_keys** | [**List[PeeringConnectionResIpv4AuthKeys]**](PeeringConnectionResIpv4AuthKeys.md) |  | [optional] 
**ip_prefixes** | **List[str]** | List of IP prefixes for the BGP session | [optional] 
**enabled** | **bool** | Whether BGP IPv4 is enabled | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_connection_res_ipv4 import PeeringConnectionResIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionResIpv4 from a JSON string
peering_connection_res_ipv4_instance = PeeringConnectionResIpv4.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionResIpv4.to_json())

# convert the object into a dict
peering_connection_res_ipv4_dict = peering_connection_res_ipv4_instance.to_dict()
# create an instance of PeeringConnectionResIpv4 from a dict
peering_connection_res_ipv4_from_dict = PeeringConnectionResIpv4.from_dict(peering_connection_res_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


