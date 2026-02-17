# ResponseUsageInputTokensDetails

A detailed breakdown of the input tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_tokens** | **int** | The number of tokens that were retrieved from the cache.  [More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).  | 

## Example

```python
from equinix.services.fabricv4.models.response_usage_input_tokens_details import ResponseUsageInputTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUsageInputTokensDetails from a JSON string
response_usage_input_tokens_details_instance = ResponseUsageInputTokensDetails.from_json(json)
# print the JSON string representation of the object
print(ResponseUsageInputTokensDetails.to_json())

# convert the object into a dict
response_usage_input_tokens_details_dict = response_usage_input_tokens_details_instance.to_dict()
# create an instance of ResponseUsageInputTokensDetails from a dict
response_usage_input_tokens_details_from_dict = ResponseUsageInputTokensDetails.from_dict(response_usage_input_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


