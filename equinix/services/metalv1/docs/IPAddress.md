# IPAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | **int** | Address Family for IP Address | [optional] 
**cidr** | **int** | Cidr Size for the IP Block created. Valid values depends on the operating system being provisioned. (28..32 for IPv4 addresses, 124..127 for IPv6 addresses) | [optional] 
**href** | **str** |  | [optional] 
**ip_reservations** | **List[str]** | UUIDs of any IP reservations to use when assigning IPs | [optional] 
**public** | **bool** | Address Type for IP Address | [optional] [default to True]

## Example

```python
from equinix_metal.models.ip_address import IPAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IPAddress from a JSON string
ip_address_instance = IPAddress.from_json(json)
# print the JSON string representation of the object
print(IPAddress.to_json())

# convert the object into a dict
ip_address_dict = ip_address_instance.to_dict()
# create an instance of IPAddress from a dict
ip_address_form_dict = ip_address.from_dict(ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


