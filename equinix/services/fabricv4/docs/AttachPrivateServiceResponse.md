# AttachPrivateServiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to the attached private service | [optional] 
**type** | **str** | Type of the private service or attachment | 
**uuid** | **str** | Unique identifier for the private service | 
**attachment_status** | **str** | Status of the attachment operation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.attach_private_service_response import AttachPrivateServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachPrivateServiceResponse from a JSON string
attach_private_service_response_instance = AttachPrivateServiceResponse.from_json(json)
# print the JSON string representation of the object
print(AttachPrivateServiceResponse.to_json())

# convert the object into a dict
attach_private_service_response_dict = attach_private_service_response_instance.to_dict()
# create an instance of AttachPrivateServiceResponse from a dict
attach_private_service_response_from_dict = AttachPrivateServiceResponse.from_dict(attach_private_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


