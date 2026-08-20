# LoaSimpleExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LoaFieldName**](LoaFieldName.md) |  | [optional] 
**operator** | [**LoaSimpleExpressionOperator**](LoaSimpleExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_simple_expression import LoaSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of LoaSimpleExpression from a JSON string
loa_simple_expression_instance = LoaSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(LoaSimpleExpression.to_json())

# convert the object into a dict
loa_simple_expression_dict = loa_simple_expression_instance.to_dict()
# create an instance of LoaSimpleExpression from a dict
loa_simple_expression_from_dict = LoaSimpleExpression.from_dict(loa_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


