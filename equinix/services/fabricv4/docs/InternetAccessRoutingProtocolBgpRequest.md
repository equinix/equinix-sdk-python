# InternetAccessRoutingProtocolBgpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[InternetAccessConnectionBgpRequest]**](InternetAccessConnectionBgpRequest.md) |  | 
**export_policy** | [**InternetAccessExportPolicy**](InternetAccessExportPolicy.md) |  | 
**customer_asn** | **int** | Customer ASN. Valid range is 1-64495 or 65536-4199999999. | [optional] 
**bgp_auth_key** | **str** | BGP authentication key | [optional] 
**customer_asn_range** | [**InternetAccessCustomerAsnRange**](InternetAccessCustomerAsnRange.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_routing_protocol_bgp_request import InternetAccessRoutingProtocolBgpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessRoutingProtocolBgpRequest from a JSON string
internet_access_routing_protocol_bgp_request_instance = InternetAccessRoutingProtocolBgpRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessRoutingProtocolBgpRequest.to_json())

# convert the object into a dict
internet_access_routing_protocol_bgp_request_dict = internet_access_routing_protocol_bgp_request_instance.to_dict()
# create an instance of InternetAccessRoutingProtocolBgpRequest from a dict
internet_access_routing_protocol_bgp_request_from_dict = InternetAccessRoutingProtocolBgpRequest.from_dict(internet_access_routing_protocol_bgp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


