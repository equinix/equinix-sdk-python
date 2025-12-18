# AttachServiceProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to the attached service profile | [optional] 
**type** | **str** | Type of the service or attachment | 
**uuid** | **str** | Unique identifier for the service profile | 
**attachment_status** | **str** | Status of the attachment operation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.attach_service_profile_response import AttachServiceProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachServiceProfileResponse from a JSON string
attach_service_profile_response_instance = AttachServiceProfileResponse.from_json(json)
# print the JSON string representation of the object
print(AttachServiceProfileResponse.to_json())

# convert the object into a dict
attach_service_profile_response_dict = attach_service_profile_response_instance.to_dict()
# create an instance of AttachServiceProfileResponse from a dict
attach_service_profile_response_from_dict = AttachServiceProfileResponse.from_dict(attach_service_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


