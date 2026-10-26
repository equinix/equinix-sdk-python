# CrossConnectAttachment

Cross Connect Attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_id** | **str** | Attachment Identifier. | 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_attachment import CrossConnectAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectAttachment from a JSON string
cross_connect_attachment_instance = CrossConnectAttachment.from_json(json)
# print the JSON string representation of the object
print(CrossConnectAttachment.to_json())

# convert the object into a dict
cross_connect_attachment_dict = cross_connect_attachment_instance.to_dict()
# create an instance of CrossConnectAttachment from a dict
cross_connect_attachment_from_dict = CrossConnectAttachment.from_dict(cross_connect_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


