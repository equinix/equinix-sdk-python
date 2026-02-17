# ResponseUsageOutputTokensDetails

A detailed breakdown of the output tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasoning_tokens** | **int** | The number of reasoning tokens. | 

## Example

```python
from equinix.services.fabricv4.models.response_usage_output_tokens_details import ResponseUsageOutputTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUsageOutputTokensDetails from a JSON string
response_usage_output_tokens_details_instance = ResponseUsageOutputTokensDetails.from_json(json)
# print the JSON string representation of the object
print(ResponseUsageOutputTokensDetails.to_json())

# convert the object into a dict
response_usage_output_tokens_details_dict = response_usage_output_tokens_details_instance.to_dict()
# create an instance of ResponseUsageOutputTokensDetails from a dict
response_usage_output_tokens_details_from_dict = ResponseUsageOutputTokensDetails.from_dict(response_usage_output_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


