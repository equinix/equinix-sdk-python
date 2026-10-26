# AppProcessorFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AppProcessorFilter]**](AppProcessorFilter.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_processor_filters import AppProcessorFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AppProcessorFilters from a JSON string
app_processor_filters_instance = AppProcessorFilters.from_json(json)
# print the JSON string representation of the object
print(AppProcessorFilters.to_json())

# convert the object into a dict
app_processor_filters_dict = app_processor_filters_instance.to_dict()
# create an instance of AppProcessorFilters from a dict
app_processor_filters_from_dict = AppProcessorFilters.from_dict(app_processor_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


