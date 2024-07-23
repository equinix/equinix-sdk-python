# ValidateRequestFilterAnd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Path to property | [optional] 
**operator** | **str** | Type of operation | [optional] 
**values** | **List[str]** | Values for the given property | [optional] 

## Example

```python
from equinix.services.fabricv4.models.validate_request_filter_and import ValidateRequestFilterAnd

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRequestFilterAnd from a JSON string
validate_request_filter_and_instance = ValidateRequestFilterAnd.from_json(json)
# print the JSON string representation of the object
print(ValidateRequestFilterAnd.to_json())

# convert the object into a dict
validate_request_filter_and_dict = validate_request_filter_and_instance.to_dict()
# create an instance of ValidateRequestFilterAnd from a dict
validate_request_filter_and_form_dict = validate_request_filter_and.from_dict(validate_request_filter_and_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


