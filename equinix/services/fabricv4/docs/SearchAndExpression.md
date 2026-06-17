# SearchAndExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[SearchFilterExpression]**](SearchFilterExpression.md) |  | 

## Example

```python
from equinix.services.fabricv4.models.search_and_expression import SearchAndExpression

# TODO update the JSON string below
json = "{}"
# create an instance of SearchAndExpression from a JSON string
search_and_expression_instance = SearchAndExpression.from_json(json)
# print the JSON string representation of the object
print(SearchAndExpression.to_json())

# convert the object into a dict
search_and_expression_dict = search_and_expression_instance.to_dict()
# create an instance of SearchAndExpression from a dict
search_and_expression_from_dict = SearchAndExpression.from_dict(search_and_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


