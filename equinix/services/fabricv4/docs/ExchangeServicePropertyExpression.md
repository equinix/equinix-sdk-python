# ExchangeServicePropertyExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**ExchangeServicePropertyExpressionProperty**](ExchangeServicePropertyExpressionProperty.md) |  | 
**operator** | [**ExchangeServicePropertyExpressionOperator**](ExchangeServicePropertyExpressionOperator.md) |  | 
**values** | **List[str]** |  | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_property_expression import ExchangeServicePropertyExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServicePropertyExpression from a JSON string
exchange_service_property_expression_instance = ExchangeServicePropertyExpression.from_json(json)
# print the JSON string representation of the object
print(ExchangeServicePropertyExpression.to_json())

# convert the object into a dict
exchange_service_property_expression_dict = exchange_service_property_expression_instance.to_dict()
# create an instance of ExchangeServicePropertyExpression from a dict
exchange_service_property_expression_from_dict = ExchangeServicePropertyExpression.from_dict(exchange_service_property_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


