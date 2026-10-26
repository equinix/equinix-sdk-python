# CrossConnectAttachmentsResponse

List of documents attached to the Cross Connect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CrossConnectAttachmentResponse]**](CrossConnectAttachmentResponse.md) |  | [optional] [readonly] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_attachments_response import CrossConnectAttachmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectAttachmentsResponse from a JSON string
cross_connect_attachments_response_instance = CrossConnectAttachmentsResponse.from_json(json)
# print the JSON string representation of the object
print(CrossConnectAttachmentsResponse.to_json())

# convert the object into a dict
cross_connect_attachments_response_dict = cross_connect_attachments_response_instance.to_dict()
# create an instance of CrossConnectAttachmentsResponse from a dict
cross_connect_attachments_response_from_dict = CrossConnectAttachmentsResponse.from_dict(cross_connect_attachments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


