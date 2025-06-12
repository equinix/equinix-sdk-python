# ProviderSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**data** | [**List[ProvidersSearchResponse]**](ProvidersSearchResponse.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_search_response import ProviderSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSearchResponse from a JSON string
provider_search_response_instance = ProviderSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderSearchResponse.to_json())

# convert the object into a dict
provider_search_response_dict = provider_search_response_instance.to_dict()
# create an instance of ProviderSearchResponse from a dict
provider_search_response_from_dict = ProviderSearchResponse.from_dict(provider_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


