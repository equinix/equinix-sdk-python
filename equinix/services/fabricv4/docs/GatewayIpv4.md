# GatewayIpv4

Gateway IPv4 address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_ip** | **str** |  | [optional] 
**secondary_ip** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gateway_ipv4 import GatewayIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayIpv4 from a JSON string
gateway_ipv4_instance = GatewayIpv4.from_json(json)
# print the JSON string representation of the object
print(GatewayIpv4.to_json())

# convert the object into a dict
gateway_ipv4_dict = gateway_ipv4_instance.to_dict()
# create an instance of GatewayIpv4 from a dict
gateway_ipv4_from_dict = GatewayIpv4.from_dict(gateway_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


