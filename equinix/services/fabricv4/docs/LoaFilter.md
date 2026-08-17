# LoaFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LoaFieldName**](LoaFieldName.md) |  | [optional] 
**operator** | [**LoaSimpleExpressionOperator**](LoaSimpleExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[LoaSimpleExpression]**](LoaSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_filter import LoaFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LoaFilter from a JSON string
loa_filter_instance = LoaFilter.from_json(json)
# print the JSON string representation of the object
print(LoaFilter.to_json())

# convert the object into a dict
loa_filter_dict = loa_filter_instance.to_dict()
# create an instance of LoaFilter from a dict
loa_filter_from_dict = LoaFilter.from_dict(loa_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


