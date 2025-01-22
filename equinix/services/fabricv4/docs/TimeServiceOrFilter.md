# TimeServiceOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[TimeServiceSimpleExpression]**](TimeServiceSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.time_service_or_filter import TimeServiceOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TimeServiceOrFilter from a JSON string
time_service_or_filter_instance = TimeServiceOrFilter.from_json(json)
# print the JSON string representation of the object
print(TimeServiceOrFilter.to_json())

# convert the object into a dict
time_service_or_filter_dict = time_service_or_filter_instance.to_dict()
# create an instance of TimeServiceOrFilter from a dict
time_service_or_filter_from_dict = TimeServiceOrFilter.from_dict(time_service_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


