# GatewayAttachmentResponse

Schema representing a Gateway attaching or detaching on a Cloud Router. This schema defines the structure of the response returned when a Gateway is attached or detached to a Cloud Router.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**type** | [**GatewayAttachmentResponseType**](GatewayAttachmentResponseType.md) |  | [optional] 
**uuid** | **str** |  | [optional] 
**attachment_status** | [**GatewayAttachmentResponseAttachmentStatus**](GatewayAttachmentResponseAttachmentStatus.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 
**change_log** | [**Changelog**](Changelog.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.gateway_attachment_response import GatewayAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayAttachmentResponse from a JSON string
gateway_attachment_response_instance = GatewayAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(GatewayAttachmentResponse.to_json())

# convert the object into a dict
gateway_attachment_response_dict = gateway_attachment_response_instance.to_dict()
# create an instance of GatewayAttachmentResponse from a dict
gateway_attachment_response_from_dict = GatewayAttachmentResponse.from_dict(gateway_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


