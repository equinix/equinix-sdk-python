# LicenseCreateInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**licensee_product_id** | **str** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from equinix_metal.models.license_create_input import LicenseCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseCreateInput from a JSON string
license_create_input_instance = LicenseCreateInput.from_json(json)
# print the JSON string representation of the object
print(LicenseCreateInput.to_json())

# convert the object into a dict
license_create_input_dict = license_create_input_instance.to_dict()
# create an instance of LicenseCreateInput from a dict
license_create_input_form_dict = license_create_input.from_dict(license_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


