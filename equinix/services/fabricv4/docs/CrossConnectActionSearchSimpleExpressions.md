# CrossConnectActionSearchSimpleExpressions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CrossConnectActionFieldName**](CrossConnectActionFieldName.md) |  | [optional] 
**operator** | [**LoaActionSearchSimpleExpressionsOperator**](LoaActionSearchSimpleExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_search_simple_expressions import CrossConnectActionSearchSimpleExpressions

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionSearchSimpleExpressions from a JSON string
cross_connect_action_search_simple_expressions_instance = CrossConnectActionSearchSimpleExpressions.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionSearchSimpleExpressions.to_json())

# convert the object into a dict
cross_connect_action_search_simple_expressions_dict = cross_connect_action_search_simple_expressions_instance.to_dict()
# create an instance of CrossConnectActionSearchSimpleExpressions from a dict
cross_connect_action_search_simple_expressions_from_dict = CrossConnectActionSearchSimpleExpressions.from_dict(cross_connect_action_search_simple_expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


