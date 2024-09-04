# UserCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**company_url** | **str** |  | [optional] 
**customdata** | **object** |  | [optional] 
**emails** | [**List[EmailInput]**](EmailInput.md) |  | 
**first_name** | **str** |  | 
**href** | **str** |  | [optional] 
**invitation_id** | **str** |  | [optional] 
**last_name** | **str** |  | 
**level** | **str** |  | [optional] 
**nonce** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**social_accounts** | **object** |  | [optional] 
**timezone** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**two_factor_auth** | **str** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.user_create_input import UserCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateInput from a JSON string
user_create_input_instance = UserCreateInput.from_json(json)
# print the JSON string representation of the object
print(UserCreateInput.to_json())

# convert the object into a dict
user_create_input_dict = user_create_input_instance.to_dict()
# create an instance of UserCreateInput from a dict
user_create_input_form_dict = user_create_input.from_dict(user_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


