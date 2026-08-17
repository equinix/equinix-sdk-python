# ExchangeServiceResponseBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_peer_ip** | **str** |  | [optional] 
**domain_name** | **str** |  | [optional] 
**primary_route_server_ip** | **str** |  | [optional] 
**secondary_route_server_ip** | **str** |  | [optional] 
**as_set** | **str** |  | [optional] 
**mlpe_enabled** | **bool** |  | [optional] 
**md5_auth_key** | **str** |  | [optional] 
**rc_md5_auth_key** | **str** |  | [optional] 
**prefixes** | **List[str]** | List of IP prefix | [optional] 
**max_prefix_limit** | **int** |  | [optional] 
**prepend_self_enabled** | **bool** |  | [optional] 

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


