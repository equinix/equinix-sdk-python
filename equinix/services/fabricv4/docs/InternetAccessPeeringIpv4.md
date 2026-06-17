# InternetAccessPeeringIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | IPv4 prefix for the peering connection | [optional] 
**prefix_length** | **int** | Determines the size of subnet | [optional] 
**equinix_peer_ip** | **str** | IPv4 peering IP address for Equinix side | [optional] 
**customer_peer_ip** | **str** | IPv4 peering IP address for customer side | [optional] 
**equinix_vrrp_ip** | **str** | IPv4 address for Equinix VRRP IP | [optional] 
**customer_vrrp_ip** | **str** | IPv4 address for customer VRRP IP | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_peering_ipv4 import InternetAccessPeeringIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPeeringIpv4 from a JSON string
internet_access_peering_ipv4_instance = InternetAccessPeeringIpv4.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPeeringIpv4.to_json())

# convert the object into a dict
internet_access_peering_ipv4_dict = internet_access_peering_ipv4_instance.to_dict()
# create an instance of InternetAccessPeeringIpv4 from a dict
internet_access_peering_ipv4_from_dict = InternetAccessPeeringIpv4.from_dict(internet_access_peering_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


