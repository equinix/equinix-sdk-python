# ServiceToken

Create Service Tokens (v4) generates Equinix Fabric service tokens. These tokens authorize users to access protected resources and services. The tokens remove sensitive content from the environment, rather than just masking it, making the protected data impossible to unencrypt or decrypt. Resource owners can distribute the tokens to trusted partners and vendors, allowing selected third parties to work directly with Equinix network assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ServiceTokenType**](ServiceTokenType.md) |  | [optional] 
**href** | **str** | An absolute URL that is the subject of the link&#39;s context. | [optional] [readonly] 
**uuid** | **str** | Equinix-assigned service token identifier | 
**name** | **str** | Customer-provided service token name | [optional] 
**description** | **str** | Customer-provided service token description | [optional] 
**expiration_date_time** | **datetime** | Expiration date and time of the service token. | [optional] 
**connection** | [**ServiceTokenConnection**](ServiceTokenConnection.md) |  | [optional] 
**state** | [**ServiceTokenState**](ServiceTokenState.md) |  | [optional] 
**notifications** | [**List[SimplifiedNotification]**](SimplifiedNotification.md) | Service token related notifications | [optional] 
**account** | [**SimplifiedAccount**](SimplifiedAccount.md) |  | [optional] 
**changelog** | [**Changelog**](Changelog.md) |  | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_token import ServiceToken

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceToken from a JSON string
service_token_instance = ServiceToken.from_json(json)
# print the JSON string representation of the object
print(ServiceToken.to_json())

# convert the object into a dict
service_token_dict = service_token_instance.to_dict()
# create an instance of ServiceToken from a dict
service_token_form_dict = service_token.from_dict(service_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


