# GatewayAttachmentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**data** | [**List[GatewayAttachmentResponse]**](GatewayAttachmentResponse.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.gateway_attachment_list_response import GatewayAttachmentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAttachmentListResponse from a JSON string
gateway_attachment_list_response_instance = GatewayAttachmentListResponse.from_json(json)
# print the JSON string representation of the object
print(GatewayAttachmentListResponse.to_json())

# convert the object into a dict
gateway_attachment_list_response_dict = gateway_attachment_list_response_instance.to_dict()
# create an instance of GatewayAttachmentListResponse from a dict
gateway_attachment_list_response_from_dict = GatewayAttachmentListResponse.from_dict(gateway_attachment_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


