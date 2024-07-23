# PortExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[PortExpression]**](PortExpression.md) |  | [optional] 
**var_or** | [**List[PortExpression]**](PortExpression.md) |  | [optional] 
**var_property** | [**PortSearchFieldName**](PortSearchFieldName.md) |  | [optional] 
**operator** | [**ServiceTokenSearchExpressionOperator**](ServiceTokenSearchExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.port_expression import PortExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PortExpression from a JSON string
port_expression_instance = PortExpression.from_json(json)
# print the JSON string representation of the object
print(PortExpression.to_json())

# convert the object into a dict
port_expression_dict = port_expression_instance.to_dict()
# create an instance of PortExpression from a dict
port_expression_form_dict = port_expression.from_dict(port_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


