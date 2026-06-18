# InternetAccessPeeringIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | IPv6 prefix for the peering connection | [optional] 
**prefix_length** | **int** | Determines the size of subnet | [optional] 
**equinix_peer_ip** | **str** | IPv6 peering IP address for Equinix side | [optional] 
**customer_peer_ip** | **str** | IPv6 peering IP address for customer side | [optional] 
**equinix_vrrp_ip** | **str** | IPv6 address for Equinix VRRP IP | [optional] 
**customer_vrrp_ip** | **str** | IPv6 address for customer VRRP IP | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_peering_ipv6 import InternetAccessPeeringIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPeeringIpv6 from a JSON string
internet_access_peering_ipv6_instance = InternetAccessPeeringIpv6.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPeeringIpv6.to_json())

# convert the object into a dict
internet_access_peering_ipv6_dict = internet_access_peering_ipv6_instance.to_dict()
# create an instance of InternetAccessPeeringIpv6 from a dict
internet_access_peering_ipv6_from_dict = InternetAccessPeeringIpv6.from_dict(internet_access_peering_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


