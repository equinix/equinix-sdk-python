# ServiceTokenSearchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ServiceTokenSearchExpression]**](ServiceTokenSearchExpression.md) |  | [optional] 
**var_property** | [**ServiceTokenSearchFieldName**](ServiceTokenSearchFieldName.md) |  | [optional] 
**operator** | [**ServiceTokenSearchExpressionOperator**](ServiceTokenSearchExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.service_token_search_expression import ServiceTokenSearchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTokenSearchExpression from a JSON string
service_token_search_expression_instance = ServiceTokenSearchExpression.from_json(json)
# print the JSON string representation of the object
print(ServiceTokenSearchExpression.to_json())

# convert the object into a dict
service_token_search_expression_dict = service_token_search_expression_instance.to_dict()
# create an instance of ServiceTokenSearchExpression from a dict
service_token_search_expression_form_dict = service_token_search_expression.from_dict(service_token_search_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


