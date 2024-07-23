# Expression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[Expression]**](Expression.md) |  | [optional] 
**var_or** | [**List[Expression]**](Expression.md) |  | [optional] 
**var_property** | [**SearchFieldName**](SearchFieldName.md) |  | [optional] 
**operator** | [**ExpressionOperator**](ExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.expression import Expression

# TODO update the JSON string below
json = "{}"
# create an instance of Expression from a JSON string
expression_instance = Expression.from_json(json)
# print the JSON string representation of the object
print(Expression.to_json())

# convert the object into a dict
expression_dict = expression_instance.to_dict()
# create an instance of Expression from a dict
expression_form_dict = expression.from_dict(expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


