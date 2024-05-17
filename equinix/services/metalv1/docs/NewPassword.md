# NewPassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**new_password** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.new_password import NewPassword

# TODO update the JSON string below
json = "{}"
# create an instance of NewPassword from a JSON string
new_password_instance = NewPassword.from_json(json)
# print the JSON string representation of the object
print(NewPassword.to_json())

# convert the object into a dict
new_password_dict = new_password_instance.to_dict()
# create an instance of NewPassword from a dict
new_password_form_dict = new_password.from_dict(new_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


