# DirectConnectionIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equinix_iface_ip** | **str** | Equinix side Interface IP address | [optional] 

## Example

```python
from equinix.services.fabricv4.models.direct_connection_ipv4 import DirectConnectionIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of DirectConnectionIpv4 from a JSON string
direct_connection_ipv4_instance = DirectConnectionIpv4.from_json(json)
# print the JSON string representation of the object
print(DirectConnectionIpv4.to_json())

# convert the object into a dict
direct_connection_ipv4_dict = direct_connection_ipv4_instance.to_dict()
# create an instance of DirectConnectionIpv4 from a dict
direct_connection_ipv4_form_dict = direct_connection_ipv4.from_dict(direct_connection_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


