# PeeringConnectionResIpv6

BGP IPv6 Connection Details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** | Customer peer IPv6 address | [optional] 
**primary_equinix_peer_ip** | **str** | Primary Equinix peer IPv6 address | [optional] 
**secondary_equinix_peer_ip** | **str** | Secondary Equinix peer IPv6 address | [optional] 
**reverse_dns_address** | **str** | Reverse DNS address for the BGP session | [optional] 
**as_set** | **str** | Autonomous System Set for the BGP session | [optional] 
**mlpe_enabled** | **bool** | Whether MLPE is enabled for the BGP session | [optional] 
**auth_keys** | [**List[PeeringConnectionResIpv4AuthKeys]**](PeeringConnectionResIpv4AuthKeys.md) |  | [optional] 
**ip_prefixes** | **List[str]** | List of IP prefixes for the BGP session | [optional] 
**enabled** | **bool** | Whether BGP IPv6 is enabled | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_connection_res_ipv6 import PeeringConnectionResIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionResIpv6 from a JSON string
peering_connection_res_ipv6_instance = PeeringConnectionResIpv6.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionResIpv6.to_json())

# convert the object into a dict
peering_connection_res_ipv6_dict = peering_connection_res_ipv6_instance.to_dict()
# create an instance of PeeringConnectionResIpv6 from a dict
peering_connection_res_ipv6_from_dict = PeeringConnectionResIpv6.from_dict(peering_connection_res_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


