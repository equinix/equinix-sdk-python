# SearchExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[SearchExpression]**](SearchExpression.md) |  | [optional] 
**var_or** | [**List[SearchExpression]**](SearchExpression.md) |  | [optional] 
**var_property** | **str** |  | [optional] 
**operator** | [**SearchExpressionOperator**](SearchExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.search_expression import SearchExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExpression from a JSON string
search_expression_instance = SearchExpression.from_json(json)
# print the JSON string representation of the object
print(SearchExpression.to_json())

# convert the object into a dict
search_expression_dict = search_expression_instance.to_dict()
# create an instance of SearchExpression from a dict
search_expression_from_dict = SearchExpression.from_dict(search_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


