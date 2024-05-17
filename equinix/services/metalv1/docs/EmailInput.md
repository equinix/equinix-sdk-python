# EmailInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**default** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.email_input import EmailInput

# TODO update the JSON string below
json = "{}"
# create an instance of EmailInput from a JSON string
email_input_instance = EmailInput.from_json(json)
# print the JSON string representation of the object
print(EmailInput.to_json())

# convert the object into a dict
email_input_dict = email_input_instance.to_dict()
# create an instance of EmailInput from a dict
email_input_form_dict = email_input.from_dict(email_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


