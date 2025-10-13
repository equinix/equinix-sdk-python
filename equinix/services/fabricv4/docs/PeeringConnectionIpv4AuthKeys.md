# PeeringConnectionIpv4AuthKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.peering_connection_ipv4_auth_keys import PeeringConnectionIpv4AuthKeys

# TODO update the JSON string below
json = "{}"
# create an instance of PeeringConnectionIpv4AuthKeys from a JSON string
peering_connection_ipv4_auth_keys_instance = PeeringConnectionIpv4AuthKeys.from_json(json)
# print the JSON string representation of the object
print(PeeringConnectionIpv4AuthKeys.to_json())

# convert the object into a dict
peering_connection_ipv4_auth_keys_dict = peering_connection_ipv4_auth_keys_instance.to_dict()
# create an instance of PeeringConnectionIpv4AuthKeys from a dict
peering_connection_ipv4_auth_keys_from_dict = PeeringConnectionIpv4AuthKeys.from_dict(peering_connection_ipv4_auth_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


