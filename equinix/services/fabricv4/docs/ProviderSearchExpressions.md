# ProviderSearchExpressions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**SearchProviderField**](SearchProviderField.md) |  | [optional] 
**operator** | [**DeploymentSearchExpressionsOperator**](DeploymentSearchExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_search_expressions import ProviderSearchExpressions

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSearchExpressions from a JSON string
provider_search_expressions_instance = ProviderSearchExpressions.from_json(json)
# print the JSON string representation of the object
print(ProviderSearchExpressions.to_json())

# convert the object into a dict
provider_search_expressions_dict = provider_search_expressions_instance.to_dict()
# create an instance of ProviderSearchExpressions from a dict
provider_search_expressions_from_dict = ProviderSearchExpressions.from_dict(provider_search_expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


