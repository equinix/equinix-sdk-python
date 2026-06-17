# InternetAccessRoutingProtocolBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_policy** | [**InternetAccessExportPolicy**](InternetAccessExportPolicy.md) |  | 
**customer_asn** | **int** | Customer ASN. Valid range is 1-64495 or 131072-4199999999. Currently this option is only available for EIA over dedicated port. | [optional] 
**bgp_auth_key** | **str** | BGP authentication key | [optional] 
**customer_asn_range** | [**InternetAccessCustomerAsnRange**](InternetAccessCustomerAsnRange.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol_bgp import InternetAccessRoutingProtocolBgp

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocolBgp from a JSON string
internet_access_routing_protocol_bgp_instance = InternetAccessRoutingProtocolBgp.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocolBgp.to_json())

# convert the object into a dict
internet_access_routing_protocol_bgp_dict = internet_access_routing_protocol_bgp_instance.to_dict()
# create an instance of InternetAccessRoutingProtocolBgp from a dict
internet_access_routing_protocol_bgp_from_dict = InternetAccessRoutingProtocolBgp.from_dict(internet_access_routing_protocol_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


