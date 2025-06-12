# AWSProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AWSProviderType**](AWSProviderType.md) |  | 
**resources** | [**List[AWSProviderResourceResponse]**](AWSProviderResourceResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.aws_provider_response import AWSProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSProviderResponse from a JSON string
aws_provider_response_instance = AWSProviderResponse.from_json(json)
# print the JSON string representation of the object
print(AWSProviderResponse.to_json())

# convert the object into a dict
aws_provider_response_dict = aws_provider_response_instance.to_dict()
# create an instance of AWSProviderResponse from a dict
aws_provider_response_from_dict = AWSProviderResponse.from_dict(aws_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


