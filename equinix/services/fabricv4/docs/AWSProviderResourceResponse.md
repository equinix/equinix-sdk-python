# AWSProviderResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**role_arn** | **str** |  | 
**region** | **str** |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 
**id** | **str** | Virtual private gateway id. | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**required** | **bool** |  | [optional] 
**vpc_id** | **str** |  | 
**subnet_id** | **str** |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_provider_resource_response import AWSProviderResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSProviderResourceResponse from a JSON string
aws_provider_resource_response_instance = AWSProviderResourceResponse.from_json(json)
# print the JSON string representation of the object
print(AWSProviderResourceResponse.to_json())

# convert the object into a dict
aws_provider_resource_response_dict = aws_provider_resource_response_instance.to_dict()
# create an instance of AWSProviderResourceResponse from a dict
aws_provider_resource_response_from_dict = AWSProviderResourceResponse.from_dict(aws_provider_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


