# BGPConnectionIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** | Customer side peering ip | 
**equinix_peer_ip** | **str** | Equinix side peering ip | [optional] 
**enabled** | **bool** | Admin status for the BGP session | 
**outbound_as_prepend_count** | **int** | AS path prepend count | [optional] 
**inbound_med** | **int** | inbound Multi Exit Discriminator attribute | [optional] 
**outbound_med** | **int** | inbound Multi Exit Discriminator attribute | [optional] 
**operation** | [**BGPConnectionOperation**](BGPConnectionOperation.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.bgp_connection_ipv4 import BGPConnectionIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BGPConnectionIpv4 from a JSON string
bgp_connection_ipv4_instance = BGPConnectionIpv4.from_json(json)
# print the JSON string representation of the object
print(BGPConnectionIpv4.to_json())

# convert the object into a dict
bgp_connection_ipv4_dict = bgp_connection_ipv4_instance.to_dict()
# create an instance of BGPConnectionIpv4 from a dict
bgp_connection_ipv4_form_dict = bgp_connection_ipv4.from_dict(bgp_connection_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


