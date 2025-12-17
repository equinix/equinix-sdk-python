# AttachLogoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to the attached logo | [optional] 
**type** | **str** | Type of the logo or attachment | 
**uuid** | **str** | Unique identifier for the logo | 
**attachment_status** | **str** | Status of the attachment operation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.attach_logo_response import AttachLogoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachLogoResponse from a JSON string
attach_logo_response_instance = AttachLogoResponse.from_json(json)
# print the JSON string representation of the object
print(AttachLogoResponse.to_json())

# convert the object into a dict
attach_logo_response_dict = attach_logo_response_instance.to_dict()
# create an instance of AttachLogoResponse from a dict
attach_logo_response_from_dict = AttachLogoResponse.from_dict(attach_logo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


