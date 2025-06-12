# AWSDirectConnect

Direct Connect helps to identify the direct connect to use or creates new one. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SearchDirectConnectType**](SearchDirectConnectType.md) |  | 
**id** | **str** |  | [optional] 
**deployment_properties** | [**TopologyProperties**](TopologyProperties.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_direct_connect import AWSDirectConnect

# TODO update the JSON string below
json = "{}"
# create an instance of AWSDirectConnect from a JSON string
aws_direct_connect_instance = AWSDirectConnect.from_json(json)
# print the JSON string representation of the object
print(AWSDirectConnect.to_json())

# convert the object into a dict
aws_direct_connect_dict = aws_direct_connect_instance.to_dict()
# create an instance of AWSDirectConnect from a dict
aws_direct_connect_from_dict = AWSDirectConnect.from_dict(aws_direct_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


