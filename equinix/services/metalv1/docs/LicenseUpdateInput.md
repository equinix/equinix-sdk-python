# LicenseUpdateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from equinix_metal.models.license_update_input import LicenseUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUpdateInput from a JSON string
license_update_input_instance = LicenseUpdateInput.from_json(json)
# print the JSON string representation of the object
print(LicenseUpdateInput.to_json())

# convert the object into a dict
license_update_input_dict = license_update_input_instance.to_dict()
# create an instance of LicenseUpdateInput from a dict
license_update_input_form_dict = license_update_input.from_dict(license_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


