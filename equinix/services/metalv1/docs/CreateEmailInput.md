# CreateEmailInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.create_email_input import CreateEmailInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailInput from a JSON string
create_email_input_instance = CreateEmailInput.from_json(json)
# print the JSON string representation of the object
print(CreateEmailInput.to_json())

# convert the object into a dict
create_email_input_dict = create_email_input_instance.to_dict()
# create an instance of CreateEmailInput from a dict
create_email_input_form_dict = create_email_input.from_dict(create_email_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


