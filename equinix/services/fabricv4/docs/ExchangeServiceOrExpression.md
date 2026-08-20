# ExchangeServiceOrExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[ExchangeServiceSearchExpression]**](ExchangeServiceSearchExpression.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_or_expression import ExchangeServiceOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceOrExpression from a JSON string
exchange_service_or_expression_instance = ExchangeServiceOrExpression.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceOrExpression.to_json())

# convert the object into a dict
exchange_service_or_expression_dict = exchange_service_or_expression_instance.to_dict()
# create an instance of ExchangeServiceOrExpression from a dict
exchange_service_or_expression_from_dict = ExchangeServiceOrExpression.from_dict(exchange_service_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


