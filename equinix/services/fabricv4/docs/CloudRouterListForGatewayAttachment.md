# CloudRouterListForGatewayAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**data** | [**List[CloudRouterForGatewayAttachmentResponse]**](CloudRouterForGatewayAttachmentResponse.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.cloud_router_list_for_gateway_attachment import CloudRouterListForGatewayAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRouterListForGatewayAttachment from a JSON string
cloud_router_list_for_gateway_attachment_instance = CloudRouterListForGatewayAttachment.from_json(json)
# print the JSON string representation of the object
print(CloudRouterListForGatewayAttachment.to_json())

# convert the object into a dict
cloud_router_list_for_gateway_attachment_dict = cloud_router_list_for_gateway_attachment_instance.to_dict()
# create an instance of CloudRouterListForGatewayAttachment from a dict
cloud_router_list_for_gateway_attachment_from_dict = CloudRouterListForGatewayAttachment.from_dict(cloud_router_list_for_gateway_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


