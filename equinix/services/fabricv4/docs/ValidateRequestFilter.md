# ValidateRequestFilter

Filters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[ValidateRequestFilterAnd]**](ValidateRequestFilterAnd.md) |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.validate_request_filter import ValidateRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRequestFilter from a JSON string
validate_request_filter_instance = ValidateRequestFilter.from_json(json)
# print the JSON string representation of the object
print(ValidateRequestFilter.to_json())

# convert the object into a dict
validate_request_filter_dict = validate_request_filter_instance.to_dict()
# create an instance of ValidateRequestFilter from a dict
validate_request_filter_form_dict = validate_request_filter.from_dict(validate_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


