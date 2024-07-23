# DirectConnectionIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equinix_iface_ip** | **str** | Equinix side Interface IP address | 

## Example

```python
from equinix.services.fabricv4.models.direct_connection_ipv6 import DirectConnectionIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of DirectConnectionIpv6 from a JSON string
direct_connection_ipv6_instance = DirectConnectionIpv6.from_json(json)
# print the JSON string representation of the object
print(DirectConnectionIpv6.to_json())

# convert the object into a dict
direct_connection_ipv6_dict = direct_connection_ipv6_instance.to_dict()
# create an instance of DirectConnectionIpv6 from a dict
direct_connection_ipv6_form_dict = direct_connection_ipv6.from_dict(direct_connection_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


