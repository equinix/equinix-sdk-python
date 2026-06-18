# SearchSimpleExpression

Simple filter expression with property, operator, and values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | 
**operator** | [**SearchSimpleExpressionOperator**](SearchSimpleExpressionOperator.md) |  | 
**values** | **List[str]** |  | 

## Example

```python
from equinix.services.fabricv4.models.search_simple_expression import SearchSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSimpleExpression from a JSON string
search_simple_expression_instance = SearchSimpleExpression.from_json(json)
# print the JSON string representation of the object
print(SearchSimpleExpression.to_json())

# convert the object into a dict
search_simple_expression_dict = search_simple_expression_instance.to_dict()
# create an instance of SearchSimpleExpression from a dict
search_simple_expression_from_dict = SearchSimpleExpression.from_dict(search_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


