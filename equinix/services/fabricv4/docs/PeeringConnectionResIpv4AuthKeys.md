# PeeringConnectionResIpv4AuthKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PeeringConnectionResIpv4AuthKeysType**](PeeringConnectionResIpv4AuthKeysType.md) |  | [optional] 
**key** | **str** | BGP authentication key | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_connection_res_ipv4_auth_keys import PeeringConnectionResIpv4AuthKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionResIpv4AuthKeys from a JSON string
peering_connection_res_ipv4_auth_keys_instance = PeeringConnectionResIpv4AuthKeys.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionResIpv4AuthKeys.to_json())

# convert the object into a dict
peering_connection_res_ipv4_auth_keys_dict = peering_connection_res_ipv4_auth_keys_instance.to_dict()
# create an instance of PeeringConnectionResIpv4AuthKeys from a dict
peering_connection_res_ipv4_auth_keys_from_dict = PeeringConnectionResIpv4AuthKeys.from_dict(peering_connection_res_ipv4_auth_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


