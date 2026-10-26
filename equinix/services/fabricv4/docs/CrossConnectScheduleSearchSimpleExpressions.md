# CrossConnectScheduleSearchSimpleExpressions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**CrossConnectScheduleFieldName**](CrossConnectScheduleFieldName.md) |  | [optional] 
**operator** | [**CrossConnectScheduleSearchSimpleExpressionsOperator**](CrossConnectScheduleSearchSimpleExpressionsOperator.md) |  | [optional] 
**values** | **List[str]** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_schedule_search_simple_expressions import CrossConnectScheduleSearchSimpleExpressions

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectScheduleSearchSimpleExpressions from a JSON string
cross_connect_schedule_search_simple_expressions_instance = CrossConnectScheduleSearchSimpleExpressions.from_json(json)
# print the JSON string representation of the object
print(CrossConnectScheduleSearchSimpleExpressions.to_json())

# convert the object into a dict
cross_connect_schedule_search_simple_expressions_dict = cross_connect_schedule_search_simple_expressions_instance.to_dict()
# create an instance of CrossConnectScheduleSearchSimpleExpressions from a dict
cross_connect_schedule_search_simple_expressions_from_dict = CrossConnectScheduleSearchSimpleExpressions.from_dict(cross_connect_schedule_search_simple_expressions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


