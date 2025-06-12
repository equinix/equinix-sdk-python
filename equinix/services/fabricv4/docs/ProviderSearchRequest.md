# ProviderSearchRequest

Search requests containing criteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ProviderExpression**](ProviderExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_search_request import ProviderSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSearchRequest from a JSON string
provider_search_request_instance = ProviderSearchRequest.from_json(json)
# print the JSON string representation of the object
print(ProviderSearchRequest.to_json())

# convert the object into a dict
provider_search_request_dict = provider_search_request_instance.to_dict()
# create an instance of ProviderSearchRequest from a dict
provider_search_request_from_dict = ProviderSearchRequest.from_dict(provider_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


