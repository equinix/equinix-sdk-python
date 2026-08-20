# ProviderEnvironments

Service Profile Provider Environments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProviderEnvironment]**](ProviderEnvironment.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_environments import ProviderEnvironments

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderEnvironments from a JSON string
provider_environments_instance = ProviderEnvironments.from_json(json)
# print the JSON string representation of the object
print(ProviderEnvironments.to_json())

# convert the object into a dict
provider_environments_dict = provider_environments_instance.to_dict()
# create an instance of ProviderEnvironments from a dict
provider_environments_from_dict = ProviderEnvironments.from_dict(provider_environments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


