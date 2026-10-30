# ErrorAdditionalInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from equinix.services.fabricv4.models.error_additional_info_inner import ErrorAdditionalInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAdditionalInfoInner from a JSON string
error_additional_info_inner_instance = ErrorAdditionalInfoInner.from_json(json)
# print the JSON string representation of the object
print(ErrorAdditionalInfoInner.to_json())

# convert the object into a dict
error_additional_info_inner_dict = error_additional_info_inner_instance.to_dict()
# create an instance of ErrorAdditionalInfoInner from a dict
error_additional_info_inner_from_dict = ErrorAdditionalInfoInner.from_dict(error_additional_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


