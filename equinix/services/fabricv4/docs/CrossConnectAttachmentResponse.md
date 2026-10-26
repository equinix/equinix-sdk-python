# CrossConnectAttachmentResponse

Document attached to a Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URI to the attachment resource. | [optional] [readonly] 
**uuid** | **str** | Attachment resource Identifier. | [optional] [readonly] 
**type** | [**CrossConnectAttachmentResponseType**](CrossConnectAttachmentResponseType.md) |  | [optional] 
**source** | [**CrossConnectAttachmentResponseSource**](CrossConnectAttachmentResponseSource.md) |  | [optional] 
**attachment_id** | **str** | Attachment Identifier. | [optional] [readonly] 
**download_href** | **str** | URI to download the attachment file content from the Equinix attachment service.  | [optional] [readonly] 
**change_log** | [**CrossConnectChangelog**](CrossConnectChangelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_attachment_response import CrossConnectAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectAttachmentResponse from a JSON string
cross_connect_attachment_response_instance = CrossConnectAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectAttachmentResponse.to_json())

# convert the object into a dict
cross_connect_attachment_response_dict = cross_connect_attachment_response_instance.to_dict()
# create an instance of CrossConnectAttachmentResponse from a dict
cross_connect_attachment_response_from_dict = CrossConnectAttachmentResponse.from_dict(cross_connect_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


