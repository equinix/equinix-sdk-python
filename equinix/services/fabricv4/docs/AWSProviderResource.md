# AWSProviderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSVirtualPrivateGatewayType**](AWSVirtualPrivateGatewayType.md) |  | 
**role_arn** | **str** |  | 
**region** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**id** | **str** |  | [optional] 
**required** | **bool** |  | 
**vpc_id** | **str** |  | [optional] 
**subnet_id** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.aws_provider_resource import AWSProviderResource

# TODO update the JSON string below
json = "{}"
# create an instance of AWSProviderResource from a JSON string
aws_provider_resource_instance = AWSProviderResource.from_json(json)
# print the JSON string representation of the object
print(AWSProviderResource.to_json())

# convert the object into a dict
aws_provider_resource_dict = aws_provider_resource_instance.to_dict()
# create an instance of AWSProviderResource from a dict
aws_provider_resource_from_dict = AWSProviderResource.from_dict(aws_provider_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


