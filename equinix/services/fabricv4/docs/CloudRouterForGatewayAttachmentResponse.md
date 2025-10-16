# CloudRouterForGatewayAttachmentResponse

Response schema showing the Fabric Cloud Router on a Gateway Attachment. This schema defines the structure of the response showing the Cloud Router when a Gateway Attachment is done on it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**CloudRouterPostRequestBaseType**](CloudRouterPostRequestBaseType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 
**attachment_status** | [**GatewayAttachmentResponseAttachmentStatus**](GatewayAttachmentResponseAttachmentStatus.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_for_gateway_attachment_response import CloudRouterForGatewayAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterForGatewayAttachmentResponse from a JSON string
cloud_router_for_gateway_attachment_response_instance = CloudRouterForGatewayAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(CloudRouterForGatewayAttachmentResponse.to_json())

# convert the object into a dict
cloud_router_for_gateway_attachment_response_dict = cloud_router_for_gateway_attachment_response_instance.to_dict()
# create an instance of CloudRouterForGatewayAttachmentResponse from a dict
cloud_router_for_gateway_attachment_response_from_dict = CloudRouterForGatewayAttachmentResponse.from_dict(cloud_router_for_gateway_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


