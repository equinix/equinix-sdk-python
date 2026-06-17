# SearchOrExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[SearchFilterExpression]**](SearchFilterExpression.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.search_or_expression import SearchOrExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOrExpression from a JSON string
search_or_expression_instance = SearchOrExpression.from_json(json)
# print the JSON string representation of the object
print(SearchOrExpression.to_json())

# convert the object into a dict
search_or_expression_dict = search_or_expression_instance.to_dict()
# create an instance of SearchOrExpression from a dict
search_or_expression_from_dict = SearchOrExpression.from_dict(search_or_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


