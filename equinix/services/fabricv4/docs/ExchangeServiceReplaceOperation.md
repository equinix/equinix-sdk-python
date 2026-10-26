# ExchangeServiceReplaceOperation

Replace attribute value or sub-resource in the existing model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | [**ExchangeServiceOpEnum**](ExchangeServiceOpEnum.md) |  | 
**path** | **str** | ### A JSON Pointer path.   * &#x60;/name&#x60; - Name of the Internet Exchange Service   * &#x60;/description&#x60; - Description of the Internet Exchange Service   * &#x60;routingProtocol/macAddress&#x60; - MAC Address   * &#x60;routingProtocol/bgpIpv4/domainName&#x60; - Domain Name for BGP IPv4   * &#x60;routingProtocol/bgpIpv4/asSet&#x60; - AS Set for BGP IPv4   * &#x60;routingProtocol/bgpIpv4/md5AuthKey&#x60; - MD5 Auth Key for BGP IPv4   * &#x60;routingProtocol/bgpIpv4/rcMd5AuthKey&#x60; - RC MD5 Auth Key for BGP IPv4   * &#x60;routingProtocol/bgpIpv4/ipPrefixes&#x60; - IP Prefixes for BGP IPv4   * &#x60;routingProtocol/bgpIpv6/mlpeEnabled&#x60; - MLPE Enabled for BGP IPv4   * &#x60;routingProtocol/bgpIpv6/domainName&#x60;- Domain Name for BGP IPv6   * &#x60;routingProtocol/bgpIpv6/asSet&#x60;- AS Set for BGP IPv6   * &#x60;routingProtocol/bgpIpv6/md5AuthKey&#x60; - MD5 Auth Key for BGP IPv6   * &#x60;routingProtocol/bgpIpv6/rcMd5AuthKey&#x60; - RC MD5 Auth Key for BGP IPv6   * &#x60;routingProtocol/bgpIpv6/ipPrefixes&#x60; - IP Prefixes for BGP IPv6   * &#x60;routingProtocol/bgpIpv6/mlpeEnabled&#x60; - MLPE Enabled for BGP IPv6  | 
**value** | **object** | value to replace with | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_replace_operation import ExchangeServiceReplaceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceReplaceOperation from a JSON string
exchange_service_replace_operation_instance = ExchangeServiceReplaceOperation.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceReplaceOperation.to_json())

# convert the object into a dict
exchange_service_replace_operation_dict = exchange_service_replace_operation_instance.to_dict()
# create an instance of ExchangeServiceReplaceOperation from a dict
exchange_service_replace_operation_from_dict = ExchangeServiceReplaceOperation.from_dict(exchange_service_replace_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


