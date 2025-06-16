# AWSVirtualPrivateGateway

The VirtualPrivateGateway schema defines the structure for the virtual private gateway configuration. It includes details about the gateway type, required flag, VPC and subnet IDs, and deployment properties. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSVirtualPrivateGatewayType**](AWSVirtualPrivateGatewayType.md) |  | 
**required** | **bool** |  | 
**vpc_id** | **str** |  | [optional] 
**subnet_id** | **str** |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_virtual_private_gateway import AWSVirtualPrivateGateway

# TODO update the JSON string below
json = "{}"
# create an instance of AWSVirtualPrivateGateway from a JSON string
aws_virtual_private_gateway_instance = AWSVirtualPrivateGateway.from_json(json)
# print the JSON string representation of the object
print(AWSVirtualPrivateGateway.to_json())

# convert the object into a dict
aws_virtual_private_gateway_dict = aws_virtual_private_gateway_instance.to_dict()
# create an instance of AWSVirtualPrivateGateway from a dict
aws_virtual_private_gateway_from_dict = AWSVirtualPrivateGateway.from_dict(aws_virtual_private_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


