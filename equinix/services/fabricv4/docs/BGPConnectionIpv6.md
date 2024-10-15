# BGPConnectionIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** | Customer side peering ip | 
**equinix_peer_ip** | **str** | Equinix side peering ip | [optional] 
**enabled** | **bool** | Admin status for the BGP session | 
**outbound_as_prepend_count** | **int** | AS path prepend count | [optional] 
**inbound_med** | **int** | Inbound Multi Exit Discriminator attribute | [optional] 
**outbound_med** | **int** | Outbound Multi Exit Discriminator attribute | [optional] 
**routes_max** | **int** | Maximum learnt prefixes limit | [optional] 
**operation** | [**BGPConnectionOperation**](BGPConnectionOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bgp_connection_ipv6 import BGPConnectionIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of BGPConnectionIpv6 from a JSON string
bgp_connection_ipv6_instance = BGPConnectionIpv6.from_json(json)
# print the JSON string representation of the object
print(BGPConnectionIpv6.to_json())

# convert the object into a dict
bgp_connection_ipv6_dict = bgp_connection_ipv6_instance.to_dict()
# create an instance of BGPConnectionIpv6 from a dict
bgp_connection_ipv6_form_dict = bgp_connection_ipv6.from_dict(bgp_connection_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


