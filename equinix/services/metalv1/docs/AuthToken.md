# AuthToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** | Available only for API keys | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | [**AuthTokenProject**](AuthTokenProject.md) |  | [optional] 
**read_only** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**AuthTokenUser**](AuthTokenUser.md) |  | [optional] 

## Example

```python
from equinix_metal.models.auth_token import AuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of AuthToken from a JSON string
auth_token_instance = AuthToken.from_json(json)
# print the JSON string representation of the object
print(AuthToken.to_json())

# convert the object into a dict
auth_token_dict = auth_token_instance.to_dict()
# create an instance of AuthToken from a dict
auth_token_form_dict = auth_token.from_dict(auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


