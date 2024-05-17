# UserLimited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_thumb_url** | **str** | Avatar thumbnail URL of the User | [optional] 
**avatar_url** | **str** | Avatar URL of the User | [optional] 
**full_name** | **str** | Full name of the User | [optional] 
**href** | **str** | API URL uniquely representing the User | [optional] 
**id** | **str** | ID of the User | 

## Example

```python
from equinix_metal.models.user_limited import UserLimited

# TODO update the JSON string below
json = "{}"
# create an instance of UserLimited from a JSON string
user_limited_instance = UserLimited.from_json(json)
# print the JSON string representation of the object
print(UserLimited.to_json())

# convert the object into a dict
user_limited_dict = user_limited_instance.to_dict()
# create an instance of UserLimited from a dict
user_limited_form_dict = user_limited.from_dict(user_limited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


