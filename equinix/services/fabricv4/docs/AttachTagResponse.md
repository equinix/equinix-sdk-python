# AttachTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to the attached tag | [optional] 
**type** | **str** | Type of the tag or attachment | 
**uuid** | **str** | Unique identifier for the tag | 
**attachment_status** | **str** | Status of the attachment operation | [optional] 

## Example

```python
from equinix.services.fabricv4.models.attach_tag_response import AttachTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachTagResponse from a JSON string
attach_tag_response_instance = AttachTagResponse.from_json(json)
# print the JSON string representation of the object
print(AttachTagResponse.to_json())

# convert the object into a dict
attach_tag_response_dict = attach_tag_response_instance.to_dict()
# create an instance of AttachTagResponse from a dict
attach_tag_response_from_dict = AttachTagResponse.from_dict(attach_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


