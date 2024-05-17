# VerifyEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**user_token** | **str** | User verification token | 

## Example

```python
from equinix_metal.models.verify_email import VerifyEmail

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmail from a JSON string
verify_email_instance = VerifyEmail.from_json(json)
# print the JSON string representation of the object
print(VerifyEmail.to_json())

# convert the object into a dict
verify_email_dict = verify_email_instance.to_dict()
# create an instance of VerifyEmail from a dict
verify_email_form_dict = verify_email.from_dict(verify_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


