# AWSVirtualPrivateGatewayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Virtual private gateway id. | [optional] 
**type** | **str** |  | 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**required** | **bool** |  | [optional] 
**vpc_id** | **str** |  | 
**subnet_id** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_virtual_private_gateway_response import AWSVirtualPrivateGatewayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSVirtualPrivateGatewayResponse from a JSON string
aws_virtual_private_gateway_response_instance = AWSVirtualPrivateGatewayResponse.from_json(json)
# print the JSON string representation of the object
print(AWSVirtualPrivateGatewayResponse.to_json())

# convert the object into a dict
aws_virtual_private_gateway_response_dict = aws_virtual_private_gateway_response_instance.to_dict()
# create an instance of AWSVirtualPrivateGatewayResponse from a dict
aws_virtual_private_gateway_response_from_dict = AWSVirtualPrivateGatewayResponse.from_dict(aws_virtual_private_gateway_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


