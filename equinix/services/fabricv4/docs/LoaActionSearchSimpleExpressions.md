# LoaActionSearchSimpleExpressions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LoaActionFieldName**](LoaActionFieldName.md) |  | [optional] 
**operator** | [**LoaActionSearchSimpleExpressionsOperator**](LoaActionSearchSimpleExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_search_simple_expressions import LoaActionSearchSimpleExpressions

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionSearchSimpleExpressions from a JSON string
loa_action_search_simple_expressions_instance = LoaActionSearchSimpleExpressions.from_json(json)
# print the JSON string representation of the object
print(LoaActionSearchSimpleExpressions.to_json())

# convert the object into a dict
loa_action_search_simple_expressions_dict = loa_action_search_simple_expressions_instance.to_dict()
# create an instance of LoaActionSearchSimpleExpressions from a dict
loa_action_search_simple_expressions_from_dict = LoaActionSearchSimpleExpressions.from_dict(loa_action_search_simple_expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


