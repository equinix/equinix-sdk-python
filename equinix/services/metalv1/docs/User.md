# User


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
from equinix_metal.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


