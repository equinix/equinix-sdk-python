# InternetAccessConnectionDirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Unique identifier for the connection | 
**peering_ipv4** | [**InternetAccessPeeringIpv4Request**](InternetAccessPeeringIpv4Request.md) |  | [optional] 
**peering_ipv6** | [**InternetAccessPeeringIpv6Request**](InternetAccessPeeringIpv6Request.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.internet_access_connection_direct_request import InternetAccessConnectionDirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternetAccessConnectionDirectRequest from a JSON string
internet_access_connection_direct_request_instance = InternetAccessConnectionDirectRequest.from_json(json)
# print the JSON string representation of the object
print(InternetAccessConnectionDirectRequest.to_json())

# convert the object into a dict
internet_access_connection_direct_request_dict = internet_access_connection_direct_request_instance.to_dict()
# create an instance of InternetAccessConnectionDirectRequest from a dict
internet_access_connection_direct_request_from_dict = InternetAccessConnectionDirectRequest.from_dict(internet_access_connection_direct_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


