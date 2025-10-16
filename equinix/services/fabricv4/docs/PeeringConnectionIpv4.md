# PeeringConnectionIpv4


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
from equinix.services.fabricv4.models.peering_connection_ipv4 import PeeringConnectionIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionIpv4 from a JSON string
peering_connection_ipv4_instance = PeeringConnectionIpv4.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionIpv4.to_json())

# convert the object into a dict
peering_connection_ipv4_dict = peering_connection_ipv4_instance.to_dict()
# create an instance of PeeringConnectionIpv4 from a dict
peering_connection_ipv4_from_dict = PeeringConnectionIpv4.from_dict(peering_connection_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


