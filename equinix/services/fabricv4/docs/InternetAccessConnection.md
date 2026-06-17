# InternetAccessConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI of the connection | 
**uuid** | **str** | Unique identifier for the connection | 
**peering_ipv4** | [**InternetAccessPeeringIpv4**](InternetAccessPeeringIpv4.md) |  | [optional] 
**peering_ipv6** | [**InternetAccessPeeringIpv6**](InternetAccessPeeringIpv6.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_connection import InternetAccessConnection

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessConnection from a JSON string
internet_access_connection_instance = InternetAccessConnection.from_json(json)
# print the JSON string representation of the object
print(InternetAccessConnection.to_json())

# convert the object into a dict
internet_access_connection_dict = internet_access_connection_instance.to_dict()
# create an instance of InternetAccessConnection from a dict
internet_access_connection_from_dict = InternetAccessConnection.from_dict(internet_access_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


