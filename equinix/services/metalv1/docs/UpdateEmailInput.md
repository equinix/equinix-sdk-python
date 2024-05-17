# UpdateEmailInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** |  | [optional] 
**href** | **str** |  | [optional] 

## Example

```python
from equinix_metal.models.update_email_input import UpdateEmailInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailInput from a JSON string
update_email_input_instance = UpdateEmailInput.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailInput.to_json())

# convert the object into a dict
update_email_input_dict = update_email_input_instance.to_dict()
# create an instance of UpdateEmailInput from a dict
update_email_input_form_dict = update_email_input.from_dict(update_email_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


