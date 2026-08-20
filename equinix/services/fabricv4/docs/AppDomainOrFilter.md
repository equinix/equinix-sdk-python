# AppDomainOrFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_or** | [**List[AppDomainSimpleExpression]**](AppDomainSimpleExpression.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.app_domain_or_filter import AppDomainOrFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AppDomainOrFilter from a JSON string
app_domain_or_filter_instance = AppDomainOrFilter.from_json(json)
# print the JSON string representation of the object
print(AppDomainOrFilter.to_json())

# convert the object into a dict
app_domain_or_filter_dict = app_domain_or_filter_instance.to_dict()
# create an instance of AppDomainOrFilter from a dict
app_domain_or_filter_from_dict = AppDomainOrFilter.from_dict(app_domain_or_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


