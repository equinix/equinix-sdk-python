# AWSFabricProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AWS Account ID | 
**href** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from equinix_metal.models.aws_fabric_provider import AWSFabricProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AWSFabricProvider from a JSON string
aws_fabric_provider_instance = AWSFabricProvider.from_json(json)
# print the JSON string representation of the object
print(AWSFabricProvider.to_json())

# convert the object into a dict
aws_fabric_provider_dict = aws_fabric_provider_instance.to_dict()
# create an instance of AWSFabricProvider from a dict
aws_fabric_provider_form_dict = aws_fabric_provider.from_dict(aws_fabric_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


