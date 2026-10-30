# ValidateRequestFilterAndInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Path to property | [optional] 
**operator** | **str** | Type of operation | [optional] 
**values** | **List[str]** | Values for the given property | [optional] 

## Example

```python
from equinix.services.fabricv4.models.validate_request_filter_and_inner import ValidateRequestFilterAndInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRequestFilterAndInner from a JSON string
validate_request_filter_and_inner_instance = ValidateRequestFilterAndInner.from_json(json)
# print the JSON string representation of the object
print(ValidateRequestFilterAndInner.to_json())

# convert the object into a dict
validate_request_filter_and_inner_dict = validate_request_filter_and_inner_instance.to_dict()
# create an instance of ValidateRequestFilterAndInner from a dict
validate_request_filter_and_inner_from_dict = ValidateRequestFilterAndInner.from_dict(validate_request_filter_and_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


