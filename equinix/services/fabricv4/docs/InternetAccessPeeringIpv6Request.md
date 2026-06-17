# InternetAccessPeeringIpv6Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equinix_peer_ip** | **str** | IPv6 address of the Equinix peering IP | [optional] 
**equinix_vrrp_ip** | **str** | IPv6 address for Equinix VRRP IP | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_peering_ipv6_request import InternetAccessPeeringIpv6Request

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessPeeringIpv6Request from a JSON string
internet_access_peering_ipv6_request_instance = InternetAccessPeeringIpv6Request.from_json(json)
# print the JSON string representation of the object
print(InternetAccessPeeringIpv6Request.to_json())

# convert the object into a dict
internet_access_peering_ipv6_request_dict = internet_access_peering_ipv6_request_instance.to_dict()
# create an instance of InternetAccessPeeringIpv6Request from a dict
internet_access_peering_ipv6_request_from_dict = InternetAccessPeeringIpv6Request.from_dict(internet_access_peering_ipv6_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


