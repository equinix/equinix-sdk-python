# CrossConnectActionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CrossConnectActionFieldName**](CrossConnectActionFieldName.md) |  | [optional] 
**operator** | [**LoaActionSearchSimpleExpressionsOperator**](LoaActionSearchSimpleExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[CrossConnectActionSearchSimpleExpressions]**](CrossConnectActionSearchSimpleExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_filter import CrossConnectActionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionFilter from a JSON string
cross_connect_action_filter_instance = CrossConnectActionFilter.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionFilter.to_json())

# convert the object into a dict
cross_connect_action_filter_dict = cross_connect_action_filter_instance.to_dict()
# create an instance of CrossConnectActionFilter from a dict
cross_connect_action_filter_from_dict = CrossConnectActionFilter.from_dict(cross_connect_action_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


