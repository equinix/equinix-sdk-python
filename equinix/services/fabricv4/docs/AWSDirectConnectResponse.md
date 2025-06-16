# AWSDirectConnectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SearchDirectConnectType**](SearchDirectConnectType.md) |  | 
**id** | **str** |  | [optional] 
**state** | [**DeploymentState**](DeploymentState.md) |  | 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_direct_connect_response import AWSDirectConnectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSDirectConnectResponse from a JSON string
aws_direct_connect_response_instance = AWSDirectConnectResponse.from_json(json)
# print the JSON string representation of the object
print(AWSDirectConnectResponse.to_json())

# convert the object into a dict
aws_direct_connect_response_dict = aws_direct_connect_response_instance.to_dict()
# create an instance of AWSDirectConnectResponse from a dict
aws_direct_connect_response_from_dict = AWSDirectConnectResponse.from_dict(aws_direct_connect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


