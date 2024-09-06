# ServiceTokens

Service tokens authorize a user to access protected resources and services available on the Equinix Fabric network. The owner of the resources can distribute service tokens to third-party users (trusted partners and vendors), allowing them to directly access and work with the resources on the network without involving the resource owners.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceToken]**](ServiceToken.md) | List of Service Tokens | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_tokens import ServiceTokens

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokens from a JSON string
service_tokens_instance = ServiceTokens.from_json(json)
# print the JSON string representation of the object
print(ServiceTokens.to_json())

# convert the object into a dict
service_tokens_dict = service_tokens_instance.to_dict()
# create an instance of ServiceTokens from a dict
service_tokens_from_dict = ServiceTokens.from_dict(service_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


