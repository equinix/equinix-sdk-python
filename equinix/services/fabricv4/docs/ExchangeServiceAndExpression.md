# ExchangeServiceAndExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ExchangeServiceSearchExpression]**](ExchangeServiceSearchExpression.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.exchange_service_and_expression import ExchangeServiceAndExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeServiceAndExpression from a JSON string
exchange_service_and_expression_instance = ExchangeServiceAndExpression.from_json(json)
# print the JSON string representation of the object
print(ExchangeServiceAndExpression.to_json())

# convert the object into a dict
exchange_service_and_expression_dict = exchange_service_and_expression_instance.to_dict()
# create an instance of ExchangeServiceAndExpression from a dict
exchange_service_and_expression_from_dict = ExchangeServiceAndExpression.from_dict(exchange_service_and_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


