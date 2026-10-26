# CrossConnectActionOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[CrossConnectActionSearchSimpleExpressions]**](CrossConnectActionSearchSimpleExpressions.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.cross_connect_action_or_filter import CrossConnectActionOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CrossConnectActionOrFilter from a JSON string
cross_connect_action_or_filter_instance = CrossConnectActionOrFilter.from_json(json)
# print the JSON string representation of the object
print(CrossConnectActionOrFilter.to_json())

# convert the object into a dict
cross_connect_action_or_filter_dict = cross_connect_action_or_filter_instance.to_dict()
# create an instance of CrossConnectActionOrFilter from a dict
cross_connect_action_or_filter_from_dict = CrossConnectActionOrFilter.from_dict(cross_connect_action_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


