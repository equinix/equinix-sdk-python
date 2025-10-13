# PeeringConnectionIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse_dns_address** | **str** |  | [optional] 
**as_set** | **str** |  | [optional] 
**mlpe_enabled** | **bool** |  | [optional] 
**auth_keys** | [**List[PeeringConnectionIpv4AuthKeys]**](PeeringConnectionIpv4AuthKeys.md) |  | [optional] 
**ip_prefixes** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_connection_ipv6 import PeeringConnectionIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionIpv6 from a JSON string
peering_connection_ipv6_instance = PeeringConnectionIpv6.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionIpv6.to_json())

# convert the object into a dict
peering_connection_ipv6_dict = peering_connection_ipv6_instance.to_dict()
# create an instance of PeeringConnectionIpv6 from a dict
peering_connection_ipv6_from_dict = PeeringConnectionIpv6.from_dict(peering_connection_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


