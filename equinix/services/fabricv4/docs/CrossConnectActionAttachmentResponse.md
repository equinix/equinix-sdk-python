# CrossConnectActionAttachmentResponse

Document the action applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI to the attachment resource. | [optional] [readonly] 
**uuid** | **str** | Attachment resource Identifier. | [optional] [readonly] 
**attachment_id** | **str** | Attachment Identifier. | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_attachment_response import CrossConnectActionAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionAttachmentResponse from a JSON string
cross_connect_action_attachment_response_instance = CrossConnectActionAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionAttachmentResponse.to_json())

# convert the object into a dict
cross_connect_action_attachment_response_dict = cross_connect_action_attachment_response_instance.to_dict()
# create an instance of CrossConnectActionAttachmentResponse from a dict
cross_connect_action_attachment_response_from_dict = CrossConnectActionAttachmentResponse.from_dict(cross_connect_action_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


