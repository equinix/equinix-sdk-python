# LoaActionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**LoaActionFieldName**](LoaActionFieldName.md) |  | [optional] 
**operator** | [**LoaActionSearchSimpleExpressionsOperator**](LoaActionSearchSimpleExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[LoaActionSearchSimpleExpressions]**](LoaActionSearchSimpleExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.loa_action_filter import LoaActionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LoaActionFilter from a JSON string
loa_action_filter_instance = LoaActionFilter.from_json(json)
# print the JSON string representation of the object
print(LoaActionFilter.to_json())

# convert the object into a dict
loa_action_filter_dict = loa_action_filter_instance.to_dict()
# create an instance of LoaActionFilter from a dict
loa_action_filter_from_dict = LoaActionFilter.from_dict(loa_action_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


