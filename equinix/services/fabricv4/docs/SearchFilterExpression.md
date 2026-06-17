# SearchFilterExpression

Filter expression that can be AND, OR, or a simple expression

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[SearchFilterExpression]**](SearchFilterExpression.md) |  | 
**var_or** | [**List[SearchFilterExpression]**](SearchFilterExpression.md) |  | 
**var_property** | **str** |  | 
**operator** | [**SearchSimpleExpressionOperator**](SearchSimpleExpressionOperator.md) |  | 
**values** | **List[str]** |  | 

## Example

```python
from equinix.services.fabricv4.models.search_filter_expression import SearchFilterExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilterExpression from a JSON string
search_filter_expression_instance = SearchFilterExpression.from_json(json)
# print the JSON string representation of the object
print(SearchFilterExpression.to_json())

# convert the object into a dict
search_filter_expression_dict = search_filter_expression_instance.to_dict()
# create an instance of SearchFilterExpression from a dict
search_filter_expression_from_dict = SearchFilterExpression.from_dict(search_filter_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


