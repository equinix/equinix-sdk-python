# CrossConnectFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CrossConnectFieldName**](CrossConnectFieldName.md) |  | [optional] 
**operator** | [**LoaSimpleExpressionOperator**](LoaSimpleExpressionOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 
**var_or** | [**List[CrossConnectSearchSimpleExpressions]**](CrossConnectSearchSimpleExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_filter import CrossConnectFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectFilter from a JSON string
cross_connect_filter_instance = CrossConnectFilter.from_json(json)
# print the JSON string representation of the object
print(CrossConnectFilter.to_json())

# convert the object into a dict
cross_connect_filter_dict = cross_connect_filter_instance.to_dict()
# create an instance of CrossConnectFilter from a dict
cross_connect_filter_from_dict = CrossConnectFilter.from_dict(cross_connect_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


