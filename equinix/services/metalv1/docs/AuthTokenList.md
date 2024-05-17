# AuthTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_keys** | [**List[AuthToken]**](AuthToken.md) |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.auth_token_list import AuthTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenList from a JSON string
auth_token_list_instance = AuthTokenList.from_json(json)
# print the JSON string representation of the object
print(AuthTokenList.to_json())

# convert the object into a dict
auth_token_list_dict = auth_token_list_instance.to_dict()
# create an instance of AuthTokenList from a dict
auth_token_list_form_dict = auth_token_list.from_dict(auth_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


