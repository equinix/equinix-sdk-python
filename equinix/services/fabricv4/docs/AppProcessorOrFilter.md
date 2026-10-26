# AppProcessorOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[AppProcessorSimpleExpression]**](AppProcessorSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor_or_filter import AppProcessorOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorOrFilter from a JSON string
app_processor_or_filter_instance = AppProcessorOrFilter.from_json(json)
# print the JSON string representation of the object
print(AppProcessorOrFilter.to_json())

# convert the object into a dict
app_processor_or_filter_dict = app_processor_or_filter_instance.to_dict()
# create an instance of AppProcessorOrFilter from a dict
app_processor_or_filter_from_dict = AppProcessorOrFilter.from_dict(app_processor_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


