# AppServiceOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[AppServiceSimpleExpression]**](AppServiceSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_service_or_filter import AppServiceOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppServiceOrFilter from a JSON string
app_service_or_filter_instance = AppServiceOrFilter.from_json(json)
# print the JSON string representation of the object
print(AppServiceOrFilter.to_json())

# convert the object into a dict
app_service_or_filter_dict = app_service_or_filter_instance.to_dict()
# create an instance of AppServiceOrFilter from a dict
app_service_or_filter_from_dict = AppServiceOrFilter.from_dict(app_service_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


