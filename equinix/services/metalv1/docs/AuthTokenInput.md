# AuthTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 

## Example

```python
from equinix_metal.models.auth_token_input import AuthTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenInput from a JSON string
auth_token_input_instance = AuthTokenInput.from_json(json)
# print the JSON string representation of the object
print(AuthTokenInput.to_json())

# convert the object into a dict
auth_token_input_dict = auth_token_input_instance.to_dict()
# create an instance of AuthTokenInput from a dict
auth_token_input_form_dict = auth_token_input.from_dict(auth_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


