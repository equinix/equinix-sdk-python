# UserUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customdata** | **object** |  | [optional] 
**first_name** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.user_update_input import UserUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateInput from a JSON string
user_update_input_instance = UserUpdateInput.from_json(json)
# print the JSON string representation of the object
print(UserUpdateInput.to_json())

# convert the object into a dict
user_update_input_dict = user_update_input_instance.to_dict()
# create an instance of UserUpdateInput from a dict
user_update_input_form_dict = user_update_input.from_dict(user_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


