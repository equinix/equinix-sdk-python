# ExchangeServiceResponseBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** | Customer peer IP address | [optional] 
**domain_name** | **str** | Domain name for BGP | [optional] 
**primary_route_server_ip** | **str** | Primary route server IP address with prefix length | [optional] 
**secondary_route_server_ip** | **str** | Secondary route server IP address with prefix length | [optional] 
**as_set** | **str** | AS-SET used to filter the prefixes announced by the customer | [optional] 
**mlpe_enabled** | **bool** | Whether Multi-Lateral Peering Exchange (MLPE) is enabled | [optional] 
**md5_auth_key** | **str** | MD5 key for BGP | [optional] 
**rc_md5_auth_key** | **str** | RC MD5 key for BGP | [optional] 
**prefixes** | **List[str]** | List of IP prefix | [optional] 
**max_prefix_limit** | **int** | Max Prefix Limit number | [optional] 
**prepend_self_enabled** | **bool** | Prepend Self Enabled | [optional] 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_response_bgp import ExchangeServiceResponseBgp

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceResponseBgp from a JSON string
exchange_service_response_bgp_instance = ExchangeServiceResponseBgp.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceResponseBgp.to_json())

# convert the object into a dict
exchange_service_response_bgp_dict = exchange_service_response_bgp_instance.to_dict()
# create an instance of ExchangeServiceResponseBgp from a dict
exchange_service_response_bgp_from_dict = ExchangeServiceResponseBgp.from_dict(exchange_service_response_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


