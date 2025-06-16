# FabricBGPConnectionIpv4

Defines the structure for a BGP IPv4 connection, including customer and Equinix peering IP addresses. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ip** | **str** | Customer side peering ip | [optional] 
**equinix_ip** | **str** | Equinix side peering ip | 

## Example

```python
from equinix.services.fabricv4.models.fabric_bgp_connection_ipv4 import FabricBGPConnectionIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of FabricBGPConnectionIpv4 from a JSON string
fabric_bgp_connection_ipv4_instance = FabricBGPConnectionIpv4.from_json(json)
# print the JSON string representation of the object
print(FabricBGPConnectionIpv4.to_json())

# convert the object into a dict
fabric_bgp_connection_ipv4_dict = fabric_bgp_connection_ipv4_instance.to_dict()
# create an instance of FabricBGPConnectionIpv4 from a dict
fabric_bgp_connection_ipv4_from_dict = FabricBGPConnectionIpv4.from_dict(fabric_bgp_connection_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


