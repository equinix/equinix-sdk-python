# ProviderExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ProviderSearchExpressions]**](ProviderSearchExpressions.md) |  | [optional] 
**var_or** | [**List[ProviderSearchExpressions]**](ProviderSearchExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.provider_expression import ProviderExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderExpression from a JSON string
provider_expression_instance = ProviderExpression.from_json(json)
# print the JSON string representation of the object
print(ProviderExpression.to_json())

# convert the object into a dict
provider_expression_dict = provider_expression_instance.to_dict()
# create an instance of ProviderExpression from a dict
provider_expression_from_dict = ProviderExpression.from_dict(provider_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


