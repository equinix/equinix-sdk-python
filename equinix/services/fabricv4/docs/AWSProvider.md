# AWSProvider

The Orchestrator AWS Providers schema defines the structure for the orchestrator aws provider configuration. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSProviderType**](AWSProviderType.md) |  | 
**resources** | [**List[AWSProviderResource]**](AWSProviderResource.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.aws_provider import AWSProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AWSProvider from a JSON string
aws_provider_instance = AWSProvider.from_json(json)
# print the JSON string representation of the object
print(AWSProvider.to_json())

# convert the object into a dict
aws_provider_dict = aws_provider_instance.to_dict()
# create an instance of AWSProvider from a dict
aws_provider_from_dict = AWSProvider.from_dict(aws_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


