# ExchangeServiceSearchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ExchangeServiceSearchExpression]**](ExchangeServiceSearchExpression.md) |  | 
**var_or** | [**List[ExchangeServiceSearchExpression]**](ExchangeServiceSearchExpression.md) |  | 
**var_property** | [**ExchangeServicePropertyExpressionProperty**](ExchangeServicePropertyExpressionProperty.md) |  | 
**operator** | [**ExchangeServicePropertyExpressionOperator**](ExchangeServicePropertyExpressionOperator.md) |  | 
**values** | **List[str]** |  | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_search_expression import ExchangeServiceSearchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceSearchExpression from a JSON string
exchange_service_search_expression_instance = ExchangeServiceSearchExpression.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceSearchExpression.to_json())

# convert the object into a dict
exchange_service_search_expression_dict = exchange_service_search_expression_instance.to_dict()
# create an instance of ExchangeServiceSearchExpression from a dict
exchange_service_search_expression_from_dict = ExchangeServiceSearchExpression.from_dict(exchange_service_search_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


