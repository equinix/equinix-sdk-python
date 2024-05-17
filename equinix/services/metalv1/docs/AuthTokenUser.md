# AuthTokenUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_thumb_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**customdata** | **object** |  | [optional] 
**default_organization_id** | **str** |  | [optional] 
**default_project_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**emails** | [**List[Href]**](Href.md) |  | [optional] 
**first_name** | **str** |  | [optional] 
**fraud_score** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_login_at** | **datetime** |  | [optional] 
**last_name** | **str** |  | [optional] 
**max_organizations** | **int** |  | [optional] 
**max_projects** | **int** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**short_id** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**two_factor_auth** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from equinix_metal.models.auth_token_user import AuthTokenUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuthTokenUser from a JSON string
auth_token_user_instance = AuthTokenUser.from_json(json)
# print the JSON string representation of the object
print(AuthTokenUser.to_json())

# convert the object into a dict
auth_token_user_dict = auth_token_user_instance.to_dict()
# create an instance of AuthTokenUser from a dict
auth_token_user_form_dict = auth_token_user.from_dict(auth_token_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


